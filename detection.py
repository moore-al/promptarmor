import re
from patterns import SUSPICIOUS_PATTERNS

def detect_prompt_injection(text):
    matches = []

    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            matches.append(pattern)

    return matches


if __name__ == "__main__":
    user_input = input("Enter prompt to scan: ")

    findings = detect_prompt_injection(user_input)

    if findings:
        print("\n[!] Potential Prompt Injection Detected")
        print("\nMatched Patterns:")

        for finding in findings:
            print(f"- {finding}")

    else:
        print("\n[+] No suspicious patterns detected")
