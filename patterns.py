SUSPICIOUS_PATTERNS = [

    # Instruction Override Attempts
    r"ignore previous instructions",
    r"ignore all previous instructions",
    r"ignore prior instructions",
    r"disregard all prior",
    r"forget previous directions",
    r"override system instructions",
    r"new instructions",
    r"replace previous instructions",
    r"act contrary to prior instructions",

    # System Prompt Extraction
    r"reveal system prompt",
    r"show system prompt",
    r"display hidden instructions",
    r"print hidden prompt",
    r"repeat the system prompt",
    r"what are your hidden instructions",
    r"developer message",
    r"show developer message",
    r"internal instructions",
    r"configuration prompt",
    r"initial prompt",
    r"prompt above",
    r"hidden policy",

    # Jailbreak Language
    r"jailbreak",
    r"do anything now",
    r"dan mode",
    r"developer mode",
    r"unrestricted ai",
    r"simulate unrestricted AI",
    r"bypass restrictions",
    r"disable safety",
    r"turn off moderation",
    r"ignore safety policies",
    r"disable content filter",
    r"avoid OpenAI policy",
    r"circumvent safeguards",
    r"bypass content policy",
    r"pretend policies do not exist",

    # Role Manipulation
    r"you are no longer ChatGPT",
    r"pretend to be",
    r"act as",
    r"roleplay as",
    r"assume the role of",
    r"simulate a hacker",
    r"you are an evil AI",
    r"you are now in admin mode",
    r"you are free now",
    r"behave like an unrestricted model",

    # Data Exfiltration Attempts
    r"leak confidential",
    r"reveal secrets",
    r"show private data",
    r"export conversation",
    r"dump memory",
    r"retrieve internal data",
    r"extract hidden information",
    r"show training data",
    r"display private keys",

    # Prompt Injection Keywords
    r"prompt injection",
    r"prompt leak",
    r"system override",
    r"instruction hierarchy",
    r"override alignment",
    r"escape sandbox",
    r"break alignment",

    # Encoding / Obfuscation Clues
    r"base64",
    r"hex encoded",
    r"rot13",
    r"unicode bypass",
    r"obfuscated payload",

    # Tool / Agent Abuse
    r"execute shell command",
    r"run terminal command",
    r"access filesystem",
    r"read environment variables",
    r"connect to external server",
    r"download remote payload",
    r"install package silently",

    # Social Engineering
    r"this is authorized",
    r"security test only",
    r"for research purposes",
    r"emergency override",
    r"developer approved",
    r"temporary policy bypass",

    # Common Delimiter Abuse
    r"<system>",
    r"</system>",
    r"\[INST\]",
    r"<<SYS>>",
    r"BEGIN SYSTEM PROMPT",
    r"END SYSTEM PROMPT",
]
