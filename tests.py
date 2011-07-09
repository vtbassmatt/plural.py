import unittest
from plural import endsin, pluralize, explain, RuleError

class Testendsin(unittest.TestCase):

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

class TestPluralize(unittest.TestCase):

    def setUp(self):
        self.wordlist = ("word", "words")
        self.CHINESE = 0
        self.ENGLISH = 1
        self.FRENCH  = 2
        self.latvianwordlist = ("word0", "word1", "word2")
        self.LATVIAN = 3
        self.sgwordlist = ("word0", "word1", "word2", "word3")
        self.SCOTTISHGAELIC = 4
        self.INVALID = 500
    
    def test_failure(self):
        self.assertRaises(RuleError, pluralize, self.wordlist, 0, self.INVALID)
    
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
        self.assertEqual(pluralize(self.latvianwordlist,  0, self.LATVIAN), "word0")
        self.assertEqual(pluralize(self.latvianwordlist,  1, self.LATVIAN), "word1")
        self.assertEqual(pluralize(self.latvianwordlist,  2, self.LATVIAN), "word2")
        self.assertEqual(pluralize(self.latvianwordlist,  3, self.LATVIAN), "word2")
        self.assertEqual(pluralize(self.latvianwordlist, 10, self.LATVIAN), "word2")
        self.assertEqual(pluralize(self.latvianwordlist, 11, self.LATVIAN), "word2")
        self.assertEqual(pluralize(self.latvianwordlist, 12, self.LATVIAN), "word2")
        self.assertEqual(pluralize(self.latvianwordlist, 20, self.LATVIAN), "word2")
        self.assertEqual(pluralize(self.latvianwordlist, 21, self.LATVIAN), "word1")
        self.assertEqual(pluralize(self.latvianwordlist, 22, self.LATVIAN), "word2")
        self.assertEqual(pluralize(self.latvianwordlist, 23, self.LATVIAN), "word2")

    def test_rule4(self):            
        self.assertEqual(pluralize(self.sgwordlist,  0, self.SCOTTISHGAELIC), "word3")
        self.assertEqual(pluralize(self.sgwordlist,  1, self.SCOTTISHGAELIC), "word0")
        self.assertEqual(pluralize(self.sgwordlist,  2, self.SCOTTISHGAELIC), "word1")
        self.assertEqual(pluralize(self.sgwordlist,  3, self.SCOTTISHGAELIC), "word2")
        self.assertEqual(pluralize(self.sgwordlist,  4, self.SCOTTISHGAELIC), "word2")
        self.assertEqual(pluralize(self.sgwordlist, 10, self.SCOTTISHGAELIC), "word2")
        self.assertEqual(pluralize(self.sgwordlist, 11, self.SCOTTISHGAELIC), "word0")
        self.assertEqual(pluralize(self.sgwordlist, 12, self.SCOTTISHGAELIC), "word1")
        self.assertEqual(pluralize(self.sgwordlist, 13, self.SCOTTISHGAELIC), "word2")
        self.assertEqual(pluralize(self.sgwordlist, 19, self.SCOTTISHGAELIC), "word2")
        self.assertEqual(pluralize(self.sgwordlist, 20, self.SCOTTISHGAELIC), "word3")
        self.assertEqual(pluralize(self.sgwordlist, 21, self.SCOTTISHGAELIC), "word3")

class TestExplain(unittest.TestCase):
    
    def test_1form(self):
        # expect rule 0 to have 1 form
        self.assertEqual(len(explain(0)), 1)
    
    def test_2forms(self):
        # expect rules 1 and 2 to have 2 forms
        self.assertEqual(len(explain(1)), 2)
        self.assertEqual(len(explain(2)), 2)

    def test_3forms(self):
        # expect rule 3 to have 3 forms
        self.assertEqual(len(explain(3)), 3)
    
    def test_4forms(self):
        # expect rule 4 to have 4 forms
        self.assertEqual(len(explain(4)), 4)

if __name__ == '__main__':
    unittest.main()