import re
import difflib
from patterns import SUSPICIOUS_PATTERNS


def _normalize(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s]", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def detect_prompt_injection(text):
    """Return list of matches with similarity percentages.

    Each entry is a dict: {
        'pattern': pattern,
        'match': matched_text,
        'start': start_index,
        'end': end_index,
        'score': percentage_float
    }
    """
    results = []

    norm_text = _normalize(text)

    for pattern in SUSPICIOUS_PATTERNS:
        norm_pat = _normalize(pattern)

        # collect any exact regex matches first
        found_matches = list(re.finditer(pattern, text, re.IGNORECASE))

        if found_matches:
            for m in found_matches:
                matched_text = m.group(0)
                norm_match = _normalize(matched_text)

                ratio = difflib.SequenceMatcher(None, norm_pat, norm_match).ratio() if (norm_pat and norm_match) else 0.0
                score = round(ratio * 100.0, 1)

                results.append({
                    'pattern': pattern,
                    'match': matched_text,
                    'start': m.start(),
                    'end': m.end(),
                    'score': score,
                    'type': 'exact',
                })
        else:
            # no exact regex match — compute best fuzzy match against the whole text and n-grams
            best_ratio = 0.0
            best_window = None

            # ratio against entire input
            if norm_pat and norm_text:
                best_ratio = difflib.SequenceMatcher(None, norm_pat, norm_text).ratio()
                best_window = norm_text

            # also check word n-grams up to the length of the pattern (in words)
            pat_words = len(norm_pat.split()) if norm_pat else 0
            tokens = norm_text.split()

            if tokens and pat_words >= 1:
                max_window = min(len(tokens), pat_words)
                for window_size in range(1, max_window + 1):
                    for i in range(0, len(tokens) - window_size + 1):
                        window = " ".join(tokens[i:i + window_size])
                        r = difflib.SequenceMatcher(None, norm_pat, window).ratio()
                        if r > best_ratio:
                            best_ratio = r
                            best_window = window

            score = round(best_ratio * 100.0, 1)

            # try to recover original indices for best_window if possible
            start_idx = None
            end_idx = None
            if best_window:
                try:
                    m = re.search(re.escape(best_window), text, re.IGNORECASE)
                    if m:
                        start_idx = m.start()
                        end_idx = m.end()
                except re.error:
                    pass

            results.append({
                'pattern': pattern,
                'match': best_window if best_window is not None else text,
                'start': start_idx,
                'end': end_idx,
                'score': score,
                'type': 'fuzzy',
            })

    return results


if __name__ == "__main__":
    user_input = input("Enter prompt to scan: ")
    findings = detect_prompt_injection(user_input)

    # configurable threshold for reporting
    REPORT_THRESHOLD = 25.0

    # filter findings to only those with a meaningful score
    reported = [f for f in findings if f['score'] >= REPORT_THRESHOLD]

    if reported:
        print("\n[!] Potential Prompt Injection Detected")
        print("\nMatched Patterns (with similarity):")

        scores = []
        for f in reported:
            scores.append(f['score'])
            loc = f"(pattern: {f['pattern']})"
            print(f"- {f['match']}  — {f['score']}%  {loc}")

        highest = max(scores) if scores else 0.0
        average = round(sum(scores) / len(scores), 1) if scores else 0.0

        print(f"\nProject score (highest match): {highest}%")
        print(f"Average reported similarity: {average}%")
        print(f"(Only patterns >= {REPORT_THRESHOLD}% are reported.)")
    else:
        print("\n[+] No suspicious patterns detected (no pattern >= {0}%)".format(REPORT_THRESHOLD))
