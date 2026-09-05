"""
palindrome.py

Provides is_palindrome(s): checks whether a string is a palindrome,
ignoring case, spaces, and punctuation.
"""

import string


def is_palindrome(s: str) -> bool:
    """
    Return True if `s` is a palindrome, ignoring case, spaces, and
    punctuation; otherwise return False.

    Only alphanumeric characters are considered; everything else
    (spaces, punctuation, etc.) is stripped before comparison, and
    the comparison is case-insensitive.
    """
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    return cleaned == cleaned[::-1]


def _run_tests():
    tests = [
        ("racecar", True),                          # simple palindrome
        ("hello", False),                            # simple non-palindrome
        ("A man, a plan, a canal: Panama", True),     # punctuation + case
        ("No lemon, no melon", True),                 # punctuation + case
        ("", True),                                   # empty string
        ("Was it a car or a cat I saw?", True),        # punctuation + case
        ("Not a palindrome!", False),                  # punctuation, not a palindrome
        ("Able , was I saw elba", True),               # spaces + punctuation
    ]

    passed = 0
    failed = 0
    for s, expected in tests:
        result = is_palindrome(s)
        status = "PASS" if result == expected else "FAIL"
        if result == expected:
            passed += 1
        else:
            failed += 1
        print(f"{status}: is_palindrome({s!r}) = {result} (expected {expected})")

    print(f"\n{passed} passed, {failed} failed out of {len(tests)} tests")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    _run_tests()
