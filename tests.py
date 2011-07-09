import unittest
from plural import endsin, index, pluralize, expects

class TestEndsIn(unittest.TestCase):

    def test_basic(self):
        self.assertTrue(endsin(  0, 0))
        self.assertTrue(endsin( 10, 0))
        self.assertTrue(endsin(100, 0))
        self.assertTrue(endsin(  1, 1))
        self.assertTrue(endsin( 11, 1))
        self.assertTrue(endsin(101, 1))
        self.assertTrue(endsin(  2, 2))
        self.assertTrue(endsin( 12, 2))
        self.assertTrue(endsin(102, 2))
        self.assertFalse(endsin(  2, 1))
        self.assertFalse(endsin( 12, 1))
        self.assertFalse(endsin(102, 1))
        
    def test_negative(self):
        self.assertTrue(endsin(  -1, 1))
        self.assertTrue(endsin( -11, 1))
        self.assertTrue(endsin(-101, 1))
        self.assertTrue(endsin(  -2, 2))
        self.assertTrue(endsin( -12, 2))
        self.assertTrue(endsin(-102, 2))
        self.assertFalse(endsin(  -2, 1))
        self.assertFalse(endsin( -12, 1))
        self.assertFalse(endsin(-102, 1))
    
    def test_typeerror(self):
        self.assertRaises(TypeError, endsin, "blah", 0)
        self.assertRaises(TypeError, endsin, 1.5, 1)

class TestIndex(unittest.TestCase):
    
    def test_rule0(self):
        self.assertEqual(index(0, 0), 0)
        self.assertEqual(index(1, 0), 0)
        self.assertEqual(index(2, 0), 0)

    def test_rule1(self):
        self.assertEqual(index(0, 1), 1)
        self.assertEqual(index(1, 1), 0)
        self.assertEqual(index(2, 1), 1)

    def test_rule2(self):
        self.assertEqual(index(0, 2), 0)
        self.assertEqual(index(1, 2), 0)
        self.assertEqual(index(2, 2), 1)

    def test_rule3(self):
        self.assertEqual(index( 0, 3), 0)
        self.assertEqual(index( 1, 3), 1)
        self.assertEqual(index( 2, 3), 2)
        self.assertEqual(index(11, 3), 2)
        self.assertEqual(index(21, 3), 1)
        self.assertEqual(index(31, 3), 1)
        self.assertEqual(index(12, 3), 2)
        self.assertEqual(index(22, 3), 2)
        self.assertEqual(index(32, 3), 2)

class TestPluralize(unittest.TestCase):

    def setUp(self):
        self.wordlist = ("word", "words")
        self.CHINESE = 0
        self.ENGLISH = 1
        self.FRENCH  = 2
        self.latvianwordlist = ("word0", "word1", "word2")
        self.LATVIAN = 3
    
    def test_rule0(self):            
        self.assertEqual(pluralize(self.wordlist, 0, self.CHINESE), "word")
        self.assertEqual(pluralize(self.wordlist, 1, self.CHINESE), "word")
        self.assertEqual(pluralize(self.wordlist, 2, self.CHINESE), "word")

    def test_rule1(self):            
        self.assertEqual(pluralize(self.wordlist, 0, self.ENGLISH), "words")
        self.assertEqual(pluralize(self.wordlist, 1, self.ENGLISH), "word")
        self.assertEqual(pluralize(self.wordlist, 2, self.ENGLISH), "words")

    def test_rule2(self):            
        self.assertEqual(pluralize(self.wordlist, 0, self.FRENCH), "word")
        self.assertEqual(pluralize(self.wordlist, 1, self.FRENCH), "word")
        self.assertEqual(pluralize(self.wordlist, 2, self.FRENCH), "words")

    def test_rule3(self):            
        self.assertEqual(pluralize(self.latvianwordlist, 0, self.LATVIAN), "word0")
        self.assertEqual(pluralize(self.latvianwordlist, 1, self.LATVIAN), "word1")
        self.assertEqual(pluralize(self.latvianwordlist, 2, self.LATVIAN), "word2")

class TestExpects(unittest.TestCase):
    
    def test_1form(self):
        # expect rule 0 to have 1 form
        self.assertEqual(len(expects(0)), 1)
    
    def test_2forms(self):
        # expect rules 1 and 2 to have 2 forms
        self.assertEqual(len(expects(1)), 2)
        self.assertEqual(len(expects(2)), 2)

    def test_3forms(self):
        # expect rule 3 to have 3 forms
        self.assertEqual(len(expects(3)), 3)

if __name__ == '__main__':
    unittest.main()