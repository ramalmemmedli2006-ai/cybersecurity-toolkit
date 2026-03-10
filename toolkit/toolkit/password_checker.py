import re


def check_password_strength(password: str) -> str:
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[^\w\s]", password):
        score += 1

    if score <= 2:
        return "Weak"
    if score == 3 or score == 4:
        return "Moderate"
    return "Strong"


def run_password_checker() -> None:
    password = input("Enter a password to evaluate: ").strip()
    result = check_password_strength(password)
    print(f"Password strength: {result}")
