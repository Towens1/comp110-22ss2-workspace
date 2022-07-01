"""Follow - along: Implementing a 'contains" Function"""
__author__ = "730237027"

def main() -> None:
    """Entrypoint of program."""
    names: list[str] = ["Kris", "Kaki"]
    print(contains("Kevin", names))

def contains(needle: str, haystack: list[str]) -> bool:
    """Return True iff needle is found in the haystack, False otherwise."""
    i: int = 0
    while i < len(haystack):
        item: str = haystack[i]
        if item == needle:
            return True
        i += 1

    return False

if __name__ == "__main__":
    main()