import unittest


def is_palindrome(s):
    """Return True if s is a palindrome, ignoring case, spaces, and punctuation."""
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]


class TestIsPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_simple_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_mixed_case(self):
        self.assertTrue(is_palindrome("RaceCar"))

    def test_punctuation_and_case(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_spaces_only(self):
        self.assertTrue(is_palindrome("nurses run"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_punctuation_non_palindrome(self):
        self.assertFalse(is_palindrome("Hello, World!"))


if __name__ == "__main__":
    unittest.main()
