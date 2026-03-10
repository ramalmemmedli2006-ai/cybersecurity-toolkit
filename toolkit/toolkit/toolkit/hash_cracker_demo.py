import hashlib


def crack_hash_demo(target_hash: str, algorithm: str, wordlist_path: str) -> str | None:
    algorithm = algorithm.lower()

    supported = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
    }

    if algorithm not in supported:
        raise ValueError("Unsupported algorithm. Use md5, sha1, or sha256.")

    with open(wordlist_path, "r", encoding="utf-8") as file:
        for line in file:
            candidate = line.strip()
            hashed = supported[algorithm](candidate.encode()).hexdigest()
            if hashed == target_hash:
                return candidate

    return None


def run_hash_cracker_demo() -> None:
    print("Supported algorithms: md5, sha1, sha256")
    algorithm = input("Enter algorithm: ").strip().lower()
    target_hash = input("Enter target hash: ").strip()

    try:
        result = crack_hash_demo(target_hash, algorithm, "wordlist.txt")
        if result:
            print(f"Match found: {result}")
        else:
            print("No match found in wordlist.")
    except ValueError as error:
        print(f"Error: {error}")
