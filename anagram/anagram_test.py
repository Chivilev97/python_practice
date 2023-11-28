import unittest
import anagram


class TestIsAnagram(unittest.TestCase):

    def test_non_anagrams(self):
        self.assertFalse(anagram.is_anagram('hello', 'hi'))
        self.assertFalse(anagram.is_anagram('', 'hi'))
        self.assertFalse(anagram.is_anagram('hello', ''))
        self.assertEqual(anagram.is_anagram('foo', 'bar'), False)

    def test_anagrams(self):
        self.assertTrue(anagram.is_anagram('', ''))
        self.assertTrue(anagram.is_anagram('note', 'tone'))
        self.assertTrue(anagram.is_anagram('silent', 'listen'))


if __name__ == '__main__':
    unittest.main()
