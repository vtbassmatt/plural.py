import unittest
from plural import _endsin, endsin1, endsin0, endsin11, endsinanyof, \
                   pluralize, explain, strrange, RuleError

# _endsin is an internal method, but there are expected to be several
# public-facing wrappers so it's worth having good test cases
class TestEndsIn(unittest.TestCase):

    def test_basic(self):
        self.assertTrue(_endsin(  0, 0))
        self.assertTrue(_endsin( 10, 0))
        self.assertTrue(_endsin(100, 0))
        self.assertTrue(_endsin(  1, 1))
        self.assertTrue(_endsin( 11, 1))
        self.assertTrue(_endsin(101, 1))
        self.assertTrue(_endsin(  2, 2))
        self.assertTrue(_endsin( 12, 2))
        self.assertTrue(_endsin(102, 2))
        self.assertFalse(_endsin(  2, 1))
        self.assertFalse(_endsin( 12, 1))
        self.assertFalse(_endsin(102, 1))
        
    def test_negative(self):
        self.assertTrue(_endsin(  -1, 1))
        self.assertTrue(_endsin( -11, 1))
        self.assertTrue(_endsin(-101, 1))
        self.assertTrue(_endsin(  -2, 2))
        self.assertTrue(_endsin( -12, 2))
        self.assertTrue(_endsin(-102, 2))
        self.assertFalse(_endsin(  -2, 1))
        self.assertFalse(_endsin( -12, 1))
        self.assertFalse(_endsin(-102, 1))
    
    def test_twodigit(self):
        self.assertTrue(_endsin(101, "01"))
        self.assertTrue(_endsin(102, "02"))
        self.assertTrue(_endsin(  2, "02"))
        self.assertTrue(_endsin( 20, "20"))
        self.assertTrue(_endsin( 99, "99"))
        self.assertTrue(_endsin( 99, 99))
        self.assertTrue(_endsin(199, "99"))
        self.assertTrue(_endsin(199, 99))
        self.assertFalse(_endsin( 22, "02"))
        self.assertFalse(_endsin(121, "01"))
    
    def test_zeroes_twodigit(self):
        self.assertTrue(_endsin(100, "00"))
        self.assertTrue(_endsin(0, "00"))
        self.assertTrue(_endsin(1000, "00"))
        self.assertFalse(_endsin(101, "00"))
    
    def test_negative_twodigit(self):
        self.assertTrue(_endsin(-102, "02"))
        self.assertTrue(_endsin(  -2, "02"))
    
    def test_typeerror(self):
        self.assertRaises(TypeError, _endsin, "blah", 0)
        self.assertRaises(TypeError, _endsin, 1.5, 1)

class TestPublicEndsIn(unittest.TestCase):
    
    def test_1(self):
        self.assertTrue(endsin1(1))
        self.assertTrue(endsin1(-1))
        self.assertTrue(endsin1(101))
        self.assertFalse(endsin1(0))
        self.assertFalse(endsin1(100))
        self.assertFalse(endsin1(111111110))
        self.assertFalse(endsin1(-2))
    
    def test_0(self):
        self.assertFalse(endsin0(1))
        self.assertFalse(endsin0(-1))
        self.assertFalse(endsin0(101))
        self.assertTrue(endsin0(0))
        self.assertTrue(endsin0(100))
        self.assertTrue(endsin0(111111110))
        self.assertFalse(endsin0(-2))

    def test_11(self):
        self.assertTrue(endsin11(11))
        self.assertTrue(endsin11(-11))
        self.assertTrue(endsin11(111))
        self.assertFalse(endsin11(0))
        self.assertFalse(endsin11(100))
        self.assertFalse(endsin11(1111111101))
        self.assertFalse(endsin11(-2))
    
class TestEndsInAnyOf(unittest.TestCase):
    
    def test_basic(self):
        self.assertTrue(endsinanyof(1, ("01","02")))
        self.assertFalse(endsinanyof(1, ("99","02")))
        self.assertTrue(endsinanyof(1, (1, 2, "01")))
        self.assertFalse(endsinanyof(1, ()))

    def test_more(self):
        self.assertTrue(endsinanyof(101, ("01","02")))
        self.assertFalse(endsinanyof(101, ("03","02")))
        self.assertTrue(endsinanyof(0, ("00", "01","02")))
        self.assertFalse(endsinanyof(0, ("01","02")))
        self.assertTrue(endsinanyof(1, ("01",)))
        self.assertTrue(endsinanyof(0, ("00",)))
        self.assertFalse(endsinanyof(0, ("01",)))

class TestStrRange(unittest.TestCase):
    
    def test_basic(self):
        self.assertEqual(strrange("00",2), ["00","01"])
        self.assertEqual(strrange("00",10), ["00","01","02","03","04","05","06","07","08","09"])
        self.assertEqual(strrange("01",10), ["01","02","03","04","05","06","07","08","09","10"])

    def test_more(self):
        self.assertEqual(strrange("99",2), ["99","100"])
        self.assertEqual(strrange("099",2), ["099","100"])
        self.assertEqual(strrange("0000",2), ["0000","0001"])

class TestPluralize(unittest.TestCase):

    def setUp(self):
        self.wordlist = ("word", "words")
        self.threewordlist = ("word0", "word1", "word2")
        self.fourwordlist = ("word0", "word1", "word2", "word3")
        self.CHINESE = 0
        self.ENGLISH = 1
        self.FRENCH  = 2
        self.LATVIAN = 3
        self.SCOTTISHGAELIC = 4
        self.ROMANIAN = 5
        self.INVALID  = 500
    
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
        self.assertEqual(pluralize(self.threewordlist,  0, self.LATVIAN), "word0")
        self.assertEqual(pluralize(self.threewordlist,  1, self.LATVIAN), "word1")
        self.assertEqual(pluralize(self.threewordlist,  2, self.LATVIAN), "word2")
        self.assertEqual(pluralize(self.threewordlist,  3, self.LATVIAN), "word2")
        self.assertEqual(pluralize(self.threewordlist, 10, self.LATVIAN), "word2")
        self.assertEqual(pluralize(self.threewordlist, 11, self.LATVIAN), "word2")
        self.assertEqual(pluralize(self.threewordlist, 12, self.LATVIAN), "word2")
        self.assertEqual(pluralize(self.threewordlist, 20, self.LATVIAN), "word2")
        self.assertEqual(pluralize(self.threewordlist, 21, self.LATVIAN), "word1")
        self.assertEqual(pluralize(self.threewordlist, 22, self.LATVIAN), "word2")
        self.assertEqual(pluralize(self.threewordlist, 23, self.LATVIAN), "word2")

    def test_rule4(self):            
        self.assertEqual(pluralize(self.fourwordlist,  0, self.SCOTTISHGAELIC), "word3")
        self.assertEqual(pluralize(self.fourwordlist,  1, self.SCOTTISHGAELIC), "word0")
        self.assertEqual(pluralize(self.fourwordlist,  2, self.SCOTTISHGAELIC), "word1")
        self.assertEqual(pluralize(self.fourwordlist,  3, self.SCOTTISHGAELIC), "word2")
        self.assertEqual(pluralize(self.fourwordlist,  4, self.SCOTTISHGAELIC), "word2")
        self.assertEqual(pluralize(self.fourwordlist, 10, self.SCOTTISHGAELIC), "word2")
        self.assertEqual(pluralize(self.fourwordlist, 11, self.SCOTTISHGAELIC), "word0")
        self.assertEqual(pluralize(self.fourwordlist, 12, self.SCOTTISHGAELIC), "word1")
        self.assertEqual(pluralize(self.fourwordlist, 13, self.SCOTTISHGAELIC), "word2")
        self.assertEqual(pluralize(self.fourwordlist, 19, self.SCOTTISHGAELIC), "word2")
        self.assertEqual(pluralize(self.fourwordlist, 20, self.SCOTTISHGAELIC), "word3")
        self.assertEqual(pluralize(self.fourwordlist, 21, self.SCOTTISHGAELIC), "word3")
    
    def test_rule5(self):
        self.assertEqual(pluralize(self.threewordlist,   0, self.ROMANIAN), "word1")
        self.assertEqual(pluralize(self.threewordlist,   1, self.ROMANIAN), "word0")
        self.assertEqual(pluralize(self.threewordlist,   2, self.ROMANIAN), "word1")
        self.assertEqual(pluralize(self.threewordlist,  19, self.ROMANIAN), "word1")
        self.assertEqual(pluralize(self.threewordlist,  20, self.ROMANIAN), "word2")
        self.assertEqual(pluralize(self.threewordlist,  21, self.ROMANIAN), "word2")
        self.assertEqual(pluralize(self.threewordlist,  99, self.ROMANIAN), "word2")
        self.assertEqual(pluralize(self.threewordlist, 100, self.ROMANIAN), "word2")
        self.assertEqual(pluralize(self.threewordlist, 101, self.ROMANIAN), "word1")
        self.assertEqual(pluralize(self.threewordlist, 109, self.ROMANIAN), "word1")

class TestRule6(unittest.TestCase):
    """For rule 6, more coverage according to the samples given by Mozilla"""

    def test_Form0(self):
        words = ("word0", "word1", "word2")
        self.assertEqual(pluralize(words,   1, 6), "word0")
        self.assertEqual(pluralize(words,  21, 6), "word0")
        self.assertEqual(pluralize(words,  31, 6), "word0")
        self.assertEqual(pluralize(words,  41, 6), "word0")
        self.assertEqual(pluralize(words,  51, 6), "word0")
        self.assertEqual(pluralize(words,  61, 6), "word0")
        self.assertEqual(pluralize(words,  71, 6), "word0")
        self.assertEqual(pluralize(words,  81, 6), "word0")
        self.assertEqual(pluralize(words,  91, 6), "word0")
        self.assertEqual(pluralize(words, 101, 6), "word0")
        self.assertEqual(pluralize(words, 121, 6), "word0")
        self.assertEqual(pluralize(words, 131, 6), "word0")
        self.assertEqual(pluralize(words, 141, 6), "word0")
        self.assertEqual(pluralize(words, 151, 6), "word0")
        self.assertEqual(pluralize(words, 161, 6), "word0")
        self.assertEqual(pluralize(words, 171, 6), "word0")
        self.assertEqual(pluralize(words, 181, 6), "word0")
        self.assertEqual(pluralize(words, 191, 6), "word0")
        self.assertEqual(pluralize(words, 201, 6), "word0")
        self.assertEqual(pluralize(words, 221, 6), "word0")
        self.assertEqual(pluralize(words, 231, 6), "word0")
        self.assertEqual(pluralize(words, 241, 6), "word0")
        self.assertEqual(pluralize(words, 251, 6), "word0")
        self.assertEqual(pluralize(words, 261, 6), "word0")
        self.assertEqual(pluralize(words, 271, 6), "word0")
        self.assertEqual(pluralize(words, 281, 6), "word0")
        self.assertEqual(pluralize(words, 291, 6), "word0")

    def test_Form1(self):
        words = ("word0", "word1", "word2")
        self.assertEqual(pluralize(words,   0, 6), "word1")
        self.assertEqual(pluralize(words,  10, 6), "word1")
        self.assertEqual(pluralize(words,  11, 6), "word1")
        self.assertEqual(pluralize(words,  12, 6), "word1")
        self.assertEqual(pluralize(words,  13, 6), "word1")
        self.assertEqual(pluralize(words,  14, 6), "word1")
        self.assertEqual(pluralize(words,  15, 6), "word1")
        self.assertEqual(pluralize(words,  16, 6), "word1")
        self.assertEqual(pluralize(words,  17, 6), "word1")
        self.assertEqual(pluralize(words,  18, 6), "word1")
        self.assertEqual(pluralize(words,  19, 6), "word1")
        self.assertEqual(pluralize(words,  20, 6), "word1")
        self.assertEqual(pluralize(words,  30, 6), "word1")
        self.assertEqual(pluralize(words,  40, 6), "word1")
        self.assertEqual(pluralize(words,  50, 6), "word1")
        self.assertEqual(pluralize(words,  60, 6), "word1")
        self.assertEqual(pluralize(words,  70, 6), "word1")
        self.assertEqual(pluralize(words,  80, 6), "word1")
        self.assertEqual(pluralize(words,  90, 6), "word1")
        self.assertEqual(pluralize(words, 100, 6), "word1")
        self.assertEqual(pluralize(words, 110, 6), "word1")
        self.assertEqual(pluralize(words, 111, 6), "word1")
        self.assertEqual(pluralize(words, 112, 6), "word1")
        self.assertEqual(pluralize(words, 113, 6), "word1")
        self.assertEqual(pluralize(words, 114, 6), "word1")
        self.assertEqual(pluralize(words, 115, 6), "word1")
        self.assertEqual(pluralize(words, 116, 6), "word1")
        self.assertEqual(pluralize(words, 117, 6), "word1")
        self.assertEqual(pluralize(words, 118, 6), "word1")
        self.assertEqual(pluralize(words, 119, 6), "word1")
        self.assertEqual(pluralize(words, 120, 6), "word1")
        self.assertEqual(pluralize(words, 130, 6), "word1")
        self.assertEqual(pluralize(words, 140, 6), "word1")
        self.assertEqual(pluralize(words, 150, 6), "word1")
        self.assertEqual(pluralize(words, 160, 6), "word1")
        self.assertEqual(pluralize(words, 170, 6), "word1")
        self.assertEqual(pluralize(words, 180, 6), "word1")
        self.assertEqual(pluralize(words, 190, 6), "word1")
        self.assertEqual(pluralize(words, 200, 6), "word1")
        self.assertEqual(pluralize(words, 210, 6), "word1")
        self.assertEqual(pluralize(words, 211, 6), "word1")
        self.assertEqual(pluralize(words, 212, 6), "word1")
        self.assertEqual(pluralize(words, 213, 6), "word1")
        self.assertEqual(pluralize(words, 214, 6), "word1")
        self.assertEqual(pluralize(words, 215, 6), "word1")
        self.assertEqual(pluralize(words, 216, 6), "word1")
        self.assertEqual(pluralize(words, 217, 6), "word1")
        self.assertEqual(pluralize(words, 218, 6), "word1")
        self.assertEqual(pluralize(words, 219, 6), "word1")
        self.assertEqual(pluralize(words, 220, 6), "word1")

    def test_Form2(self):
        words = ("word0", "word1", "word2")
        self.assertEqual(pluralize(words,   2, 6), "word2")
        self.assertEqual(pluralize(words,   3, 6), "word2")
        self.assertEqual(pluralize(words,   4, 6), "word2")
        self.assertEqual(pluralize(words,   5, 6), "word2")
        self.assertEqual(pluralize(words,   6, 6), "word2")
        self.assertEqual(pluralize(words,   7, 6), "word2")
        self.assertEqual(pluralize(words,   8, 6), "word2")
        self.assertEqual(pluralize(words,   9, 6), "word2")
        self.assertEqual(pluralize(words,  22, 6), "word2")
        self.assertEqual(pluralize(words,  23, 6), "word2")
        self.assertEqual(pluralize(words,  24, 6), "word2")
        self.assertEqual(pluralize(words,  25, 6), "word2")
        self.assertEqual(pluralize(words,  26, 6), "word2")
        self.assertEqual(pluralize(words,  27, 6), "word2")
        self.assertEqual(pluralize(words,  28, 6), "word2")
        self.assertEqual(pluralize(words,  29, 6), "word2")
        self.assertEqual(pluralize(words,  32, 6), "word2")
        self.assertEqual(pluralize(words,  33, 6), "word2")
        self.assertEqual(pluralize(words,  34, 6), "word2")
        self.assertEqual(pluralize(words,  35, 6), "word2")
        self.assertEqual(pluralize(words,  36, 6), "word2")
        self.assertEqual(pluralize(words,  37, 6), "word2")
        self.assertEqual(pluralize(words,  38, 6), "word2")
        self.assertEqual(pluralize(words,  39, 6), "word2")
        self.assertEqual(pluralize(words,  42, 6), "word2")
        self.assertEqual(pluralize(words,  43, 6), "word2")
        self.assertEqual(pluralize(words,  44, 6), "word2")
        self.assertEqual(pluralize(words,  45, 6), "word2")
        self.assertEqual(pluralize(words,  46, 6), "word2")
        self.assertEqual(pluralize(words,  47, 6), "word2")
        self.assertEqual(pluralize(words,  48, 6), "word2")
        self.assertEqual(pluralize(words,  49, 6), "word2")
        self.assertEqual(pluralize(words,  52, 6), "word2")
        self.assertEqual(pluralize(words,  53, 6), "word2")
        self.assertEqual(pluralize(words,  54, 6), "word2")
        self.assertEqual(pluralize(words,  55, 6), "word2")
        self.assertEqual(pluralize(words,  56, 6), "word2")
        self.assertEqual(pluralize(words,  57, 6), "word2")
        self.assertEqual(pluralize(words,  58, 6), "word2")
        self.assertEqual(pluralize(words,  59, 6), "word2")
        self.assertEqual(pluralize(words,  62, 6), "word2")
        self.assertEqual(pluralize(words,  63, 6), "word2")
        self.assertEqual(pluralize(words,  64, 6), "word2")
        self.assertEqual(pluralize(words,  65, 6), "word2")
        self.assertEqual(pluralize(words,  66, 6), "word2")
        self.assertEqual(pluralize(words,  67, 6), "word2")
        self.assertEqual(pluralize(words,  68, 6), "word2")
        self.assertEqual(pluralize(words,  69, 6), "word2")
        self.assertEqual(pluralize(words,  72, 6), "word2")
        self.assertEqual(pluralize(words,  73, 6), "word2")

class TestExplain(unittest.TestCase):
    
    def test_failure(self):
        self.assertRaises(RuleError, explain, 500)

    def test_1form(self):
        # expect rule 0 to have 1 form
        self.assertEqual(len(explain(0)), 1)
    
    def test_2forms(self):
        # expect rule 1, 2 to have 2 forms
        self.assertEqual(len(explain(1)), 2)
        self.assertEqual(len(explain(2)), 2)

    def test_3forms(self):
        # expect rule 3, 5-6 to have 3 forms
        self.assertEqual(len(explain(3)), 3)
        self.assertEqual(len(explain(5)), 3)
        self.assertEqual(len(explain(6)), 3)
    
    def test_4forms(self):
        # expect rule 4 to have 4 forms
        self.assertEqual(len(explain(4)), 4)

if __name__ == '__main__':
    unittest.main()