# token_regex_patterns.py

import re

# === Individual Token Pattern Detectors ===

def detect_openai_keys(text: str) -> bool:
    """Detect OpenAI-style API keys: sk-XXXXXXXXXXXXXXXX."""
    return bool(re.search(r"\bsk-[A-Za-z0-9]{16,}\b", text))

def detect_bearer_tokens(text: str) -> bool:
    """Detect Bearer token strings, common in OAuth headers."""
    return bool(re.search(r"\bBearer\s+[A-Za-z0-9\-._~+/=]+\b", text))

def detect_github_pat(text: str) -> bool:
    """Detect GitHub Personal Access Tokens: ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX."""
    return bool(re.search(r"\bghp_[A-Za-z0-9]{36}\b", text))

def detect_aws_keys(text: str) -> bool:
    """Detect AWS Access Key IDs: AKIA + 16 uppercase letters/digits."""
    return bool(re.search(r"\bAKIA[0-9A-Z]{16}\b", text))

# === Master Detector Map ===

DETECTORS = {
    "openai": detect_openai_keys,
    "bearer": detect_bearer_tokens,
    "github": detect_github_pat,
    "aws": detect_aws_keys
}

# === Bulk Runner ===

def run_all_detectors(text: str) -> dict:
    """Run all token detection functions on input text."""
    return {name: detector(text) for name, detector in DETECTORS.items()}

# === Fast Binary Check ===

def contains_any_token(text: str) -> bool:
    """Quick check to see if any known token pattern exists in text."""
    return any(run_all_detectors(text).values())