import unittest
import validate_brackets as vb

class ValidateBracketsTestCase(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(vb.validate_brackets(''))
        self.assertTrue(vb.validate_brackets('hello world'))
        self.assertTrue(vb.validate_brackets('()'))
        self.assertTrue(vb.validate_brackets('(())'))
        self.assertTrue(vb.validate_brackets('()()'))
        self.assertTrue(vb.validate_brackets('print()'))
        self.assertTrue(vb.validate_brackets('(vasya()privet)'))
        self.assertTrue(vb.validate_brackets('[]'))
        self.assertTrue(vb.validate_brackets('([])'))
        self.assertTrue(vb.validate_brackets('()[]'))
        self.assertTrue(vb.validate_brackets('()[](([[]]))'))
        self.assertTrue(vb.validate_brackets('{}'))
        self.assertTrue(vb.validate_brackets('()[]{}'))
        self.assertTrue(vb.validate_brackets('([{}])'))

    def test_invalid(self):
        self.assertFalse(vb.validate_brackets(')'))
        self.assertFalse(vb.validate_brackets('('))
        self.assertFalse(vb.validate_brackets('())'))
        self.assertFalse(vb.validate_brackets('()('))
        self.assertFalse(vb.validate_brackets('(()'))
        self.assertFalse(vb.validate_brackets('((('))
        self.assertFalse(vb.validate_brackets('))(('))
        self.assertFalse(vb.validate_brackets('['))
        self.assertFalse(vb.validate_brackets(']'))
        self.assertFalse(vb.validate_brackets('([)]'))
        self.assertFalse(vb.validate_brackets(']9[0]90[]]])([)(][)()()'))
        self.assertFalse(vb.validate_brackets('()['))
        self.assertFalse(vb.validate_brackets('{'))
        self.assertFalse(vb.validate_brackets('}'))
        self.assertFalse(vb.validate_brackets('([{})]'))



if __name__ == '__main__':
    unittest.main()
