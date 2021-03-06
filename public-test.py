import unittest
from plural import pluralize, explain, rulefor, RuleError

class TestHighLevel(unittest.TestCase):
    
    def test_basic1(self):
        self.assertEqual(pluralize(('apple','apples'), 1, rulefor('en')), 'apple')
    def test_basic2(self):
        self.assertEqual(pluralize(('apple','apples'), 2, rulefor('en')), 'apples')

class TestPluralize(unittest.TestCase):

    def setUp(self):
        self.wordlist = ("word", "words")
        self.threewordlist = ("word0", "word1", "word2")
        self.fourwordlist = ("word0", "word1", "word2", "word3")
        self.fivewordlist = ("word0", "word1", "word2", "word3", "word4")
        self.sixwordlist = ("word0", "word1", "word2", "word3", "word4", "word5")
        self.CHINESE        = 0
        self.ENGLISH        = 1
        self.FRENCH         = 2
        self.LATVIAN        = 3
        self.SCOTTISHGAELIC = 4
        self.ROMANIAN       = 5
        self.SLOVAK         = 8
        self.SLOVENIAN      = 10
        self.IRISHGAELIC    = 11
        self.ARABIC         = 12
        self.ICELANDIC      = 15
        self.INVALID        = 500
    
    def test_failure(self):
        self.assertRaises(RuleError, pluralize, self.wordlist, 0, self.INVALID)
    
    def test_rule0_1(self):            
        self.assertEqual(pluralize(self.wordlist, 0, self.CHINESE), "word")
    def test_rule0_2(self):            
        self.assertEqual(pluralize(self.wordlist, 1, self.CHINESE), "word")
    def test_rule0_3(self):            
        self.assertEqual(pluralize(self.wordlist, 2, self.CHINESE), "word")

    def test_rule1_1(self):            
        self.assertEqual(pluralize(self.wordlist, 0, self.ENGLISH), "words")
    def test_rule1_2(self):            
        self.assertEqual(pluralize(self.wordlist, 1, self.ENGLISH), "word")
    def test_rule1_3(self):            
        self.assertEqual(pluralize(self.wordlist, 2, self.ENGLISH), "words")

    def test_rule2_1(self):            
        self.assertEqual(pluralize(self.wordlist, 0, self.FRENCH), "word")
    def test_rule2_2(self):            
        self.assertEqual(pluralize(self.wordlist, 1, self.FRENCH), "word")
    def test_rule2_3(self):            
        self.assertEqual(pluralize(self.wordlist, 2, self.FRENCH), "words")

    def test_rule3_1(self):            
        self.assertEqual(pluralize(self.threewordlist,  0, self.LATVIAN), "word0")
    def test_rule3_2(self):            
        self.assertEqual(pluralize(self.threewordlist,  1, self.LATVIAN), "word1")
    def test_rule3_3(self):            
        self.assertEqual(pluralize(self.threewordlist,  2, self.LATVIAN), "word2")
    def test_rule3_4(self):            
        self.assertEqual(pluralize(self.threewordlist,  3, self.LATVIAN), "word2")
    def test_rule3_5(self):            
        self.assertEqual(pluralize(self.threewordlist, 10, self.LATVIAN), "word2")
    def test_rule3_6(self):            
        self.assertEqual(pluralize(self.threewordlist, 11, self.LATVIAN), "word2")
    def test_rule3_7(self):            
        self.assertEqual(pluralize(self.threewordlist, 12, self.LATVIAN), "word2")
    def test_rule3_8(self):            
        self.assertEqual(pluralize(self.threewordlist, 20, self.LATVIAN), "word2")
    def test_rule3_9(self):            
        self.assertEqual(pluralize(self.threewordlist, 21, self.LATVIAN), "word1")
    def test_rule3_10(self):            
        self.assertEqual(pluralize(self.threewordlist, 22, self.LATVIAN), "word2")
    def test_rule3_11(self):            
        self.assertEqual(pluralize(self.threewordlist, 23, self.LATVIAN), "word2")

    def test_rule4_1(self):            
        self.assertEqual(pluralize(self.fourwordlist,  0, self.SCOTTISHGAELIC), "word3")
    def test_rule4_2(self):            
        self.assertEqual(pluralize(self.fourwordlist,  1, self.SCOTTISHGAELIC), "word0")
    def test_rule4_3(self):            
        self.assertEqual(pluralize(self.fourwordlist,  2, self.SCOTTISHGAELIC), "word1")
    def test_rule4_4(self):            
        self.assertEqual(pluralize(self.fourwordlist,  3, self.SCOTTISHGAELIC), "word2")
    def test_rule4_5(self):            
        self.assertEqual(pluralize(self.fourwordlist,  4, self.SCOTTISHGAELIC), "word2")
    def test_rule4_6(self):            
        self.assertEqual(pluralize(self.fourwordlist, 10, self.SCOTTISHGAELIC), "word2")
    def test_rule4_7(self):            
        self.assertEqual(pluralize(self.fourwordlist, 11, self.SCOTTISHGAELIC), "word0")
    def test_rule4_8(self):            
        self.assertEqual(pluralize(self.fourwordlist, 12, self.SCOTTISHGAELIC), "word1")
    def test_rule4_9(self):            
        self.assertEqual(pluralize(self.fourwordlist, 13, self.SCOTTISHGAELIC), "word2")
    def test_rule4_10(self):            
        self.assertEqual(pluralize(self.fourwordlist, 19, self.SCOTTISHGAELIC), "word2")
    def test_rule4_11(self):            
        self.assertEqual(pluralize(self.fourwordlist, 20, self.SCOTTISHGAELIC), "word3")
    def test_rule4_12(self):            
        self.assertEqual(pluralize(self.fourwordlist, 21, self.SCOTTISHGAELIC), "word3")
    
    def test_rule5_1(self):
        self.assertEqual(pluralize(self.threewordlist,   0, self.ROMANIAN), "word1")
    def test_rule5_2(self):
        self.assertEqual(pluralize(self.threewordlist,   1, self.ROMANIAN), "word0")
    def test_rule5_3(self):
        self.assertEqual(pluralize(self.threewordlist,   2, self.ROMANIAN), "word1")
    def test_rule5_4(self):
        self.assertEqual(pluralize(self.threewordlist,  19, self.ROMANIAN), "word1")
    def test_rule5_5(self):
        self.assertEqual(pluralize(self.threewordlist,  20, self.ROMANIAN), "word2")
    def test_rule5_6(self):
        self.assertEqual(pluralize(self.threewordlist,  21, self.ROMANIAN), "word2")
    def test_rule5_7(self):
        self.assertEqual(pluralize(self.threewordlist,  99, self.ROMANIAN), "word2")
    def test_rule5_8(self):
        self.assertEqual(pluralize(self.threewordlist, 100, self.ROMANIAN), "word2")
    def test_rule5_9(self):
        self.assertEqual(pluralize(self.threewordlist, 101, self.ROMANIAN), "word1")
    def test_rule5_10(self):
        self.assertEqual(pluralize(self.threewordlist, 109, self.ROMANIAN), "word1")
    
    def test_rule8_1(self):
        self.assertEqual(pluralize(self.threewordlist,   0, self.SLOVAK), "word2")
    def test_rule8_2(self):
        self.assertEqual(pluralize(self.threewordlist,   1, self.SLOVAK), "word0")
    def test_rule8_3(self):
        self.assertEqual(pluralize(self.threewordlist,   2, self.SLOVAK), "word1")
    def test_rule8_4(self):
        self.assertEqual(pluralize(self.threewordlist,   3, self.SLOVAK), "word1")
    def test_rule8_5(self):
        self.assertEqual(pluralize(self.threewordlist,   4, self.SLOVAK), "word1")
    def test_rule8_6(self):
        self.assertEqual(pluralize(self.threewordlist,   5, self.SLOVAK), "word2")

    def test_rule10_1(self):
        self.assertEqual(pluralize(self.fourwordlist,   0, self.SLOVENIAN), "word3")
    def test_rule10_2(self):
        self.assertEqual(pluralize(self.fourwordlist,   1, self.SLOVENIAN), "word0")
    def test_rule10_3(self):
        self.assertEqual(pluralize(self.fourwordlist,   2, self.SLOVENIAN), "word1")
    def test_rule10_4(self):
        self.assertEqual(pluralize(self.fourwordlist,   3, self.SLOVENIAN), "word2")
    def test_rule10_5(self):
        self.assertEqual(pluralize(self.fourwordlist,   4, self.SLOVENIAN), "word2")
    def test_rule10_6(self):
        self.assertEqual(pluralize(self.fourwordlist,   5, self.SLOVENIAN), "word3")
    def test_rule10_7(self):
        self.assertEqual(pluralize(self.fourwordlist, 100, self.SLOVENIAN), "word3")
    def test_rule10_8(self):
        self.assertEqual(pluralize(self.fourwordlist, 101, self.SLOVENIAN), "word0")
    def test_rule10_9(self):
        self.assertEqual(pluralize(self.fourwordlist, 102, self.SLOVENIAN), "word1")
    def test_rule10_10(self):
        self.assertEqual(pluralize(self.fourwordlist, 103, self.SLOVENIAN), "word2")
    def test_rule10_11(self):
        self.assertEqual(pluralize(self.fourwordlist, 104, self.SLOVENIAN), "word2")
    def test_rule10_12(self):
        self.assertEqual(pluralize(self.fourwordlist, 105, self.SLOVENIAN), "word3")

    def test_rule11_1(self):
        self.assertEqual(pluralize(self.fivewordlist,   0, self.IRISHGAELIC), "word4")
    def test_rule11_2(self):
        self.assertEqual(pluralize(self.fivewordlist,   1, self.IRISHGAELIC), "word0")
    def test_rule11_3(self):
        self.assertEqual(pluralize(self.fivewordlist,   2, self.IRISHGAELIC), "word1")
    def test_rule11_4(self):
        self.assertEqual(pluralize(self.fivewordlist,   3, self.IRISHGAELIC), "word2")
    def test_rule11_5(self):
        self.assertEqual(pluralize(self.fivewordlist,   4, self.IRISHGAELIC), "word2")
    def test_rule11_6(self):
        self.assertEqual(pluralize(self.fivewordlist,   5, self.IRISHGAELIC), "word2")
    def test_rule11_7(self):
        self.assertEqual(pluralize(self.fivewordlist,   6, self.IRISHGAELIC), "word2")
    def test_rule11_8(self):
        self.assertEqual(pluralize(self.fivewordlist,   7, self.IRISHGAELIC), "word3")
    def test_rule11_9(self):
        self.assertEqual(pluralize(self.fivewordlist,   8, self.IRISHGAELIC), "word3")
    def test_rule11_10(self):
        self.assertEqual(pluralize(self.fivewordlist,   9, self.IRISHGAELIC), "word3")
    def test_rule11_11(self):
        self.assertEqual(pluralize(self.fivewordlist,  10, self.IRISHGAELIC), "word3")
    def test_rule11_12(self):
        self.assertEqual(pluralize(self.fivewordlist,  11, self.IRISHGAELIC), "word4")
    def test_rule11_13(self):
        self.assertEqual(pluralize(self.fivewordlist,  12, self.IRISHGAELIC), "word4")
    def test_rule11_14(self):
        self.assertEqual(pluralize(self.fivewordlist,  99, self.IRISHGAELIC), "word4")
    def test_rule11_15(self):
        self.assertEqual(pluralize(self.fivewordlist, 100, self.IRISHGAELIC), "word4")
    def test_rule11_16(self):
        self.assertEqual(pluralize(self.fivewordlist, 101, self.IRISHGAELIC), "word4")

    def test_rule12_1(self):
        self.assertEqual(pluralize(self.sixwordlist,   0, self.ARABIC), "word0")
    def test_rule12_2(self):
        self.assertEqual(pluralize(self.sixwordlist,   1, self.ARABIC), "word1")
    def test_rule12_3(self):
        self.assertEqual(pluralize(self.sixwordlist,   2, self.ARABIC), "word2")
    def test_rule12_4(self):
        self.assertEqual(pluralize(self.sixwordlist,   3, self.ARABIC), "word3")
    def test_rule12_5(self):
        self.assertEqual(pluralize(self.sixwordlist,   4, self.ARABIC), "word3")
    def test_rule12_6(self):
        self.assertEqual(pluralize(self.sixwordlist,   5, self.ARABIC), "word3")
    def test_rule12_7(self):
        self.assertEqual(pluralize(self.sixwordlist,   6, self.ARABIC), "word3")
    def test_rule12_8(self):
        self.assertEqual(pluralize(self.sixwordlist,   7, self.ARABIC), "word3")
    def test_rule12_9(self):
        self.assertEqual(pluralize(self.sixwordlist,   8, self.ARABIC), "word3")
    def test_rule12_10(self):
        self.assertEqual(pluralize(self.sixwordlist,   9, self.ARABIC), "word3")
    def test_rule12_11(self):
        self.assertEqual(pluralize(self.sixwordlist,  10, self.ARABIC), "word3")
    def test_rule12_12(self):
        self.assertEqual(pluralize(self.sixwordlist, 103, self.ARABIC), "word3")
    def test_rule12_13(self):
        self.assertEqual(pluralize(self.sixwordlist, 104, self.ARABIC), "word3")
    def test_rule12_14(self):
        self.assertEqual(pluralize(self.sixwordlist, 105, self.ARABIC), "word3")
    def test_rule12_15(self):
        self.assertEqual(pluralize(self.sixwordlist, 106, self.ARABIC), "word3")
    def test_rule12_16(self):
        self.assertEqual(pluralize(self.sixwordlist, 107, self.ARABIC), "word3")
    def test_rule12_17(self):
        self.assertEqual(pluralize(self.sixwordlist, 108, self.ARABIC), "word3")
    def test_rule12_18(self):
        self.assertEqual(pluralize(self.sixwordlist, 109, self.ARABIC), "word3")
    def test_rule12_19(self):
        self.assertEqual(pluralize(self.sixwordlist, 110, self.ARABIC), "word3")
    def test_rule12_20(self):
        self.assertEqual(pluralize(self.sixwordlist, 203, self.ARABIC), "word3")
    def test_rule12_21(self):
        self.assertEqual(pluralize(self.sixwordlist, 204, self.ARABIC), "word3")
    def test_rule12_22(self):
        self.assertEqual(pluralize(self.sixwordlist, 205, self.ARABIC), "word3")
    def test_rule12_23(self):
        self.assertEqual(pluralize(self.sixwordlist, 206, self.ARABIC), "word3")
    def test_rule12_24(self):
        self.assertEqual(pluralize(self.sixwordlist, 207, self.ARABIC), "word3")
    def test_rule12_25(self):
        self.assertEqual(pluralize(self.sixwordlist, 208, self.ARABIC), "word3")
    def test_rule12_26(self):
        self.assertEqual(pluralize(self.sixwordlist, 209, self.ARABIC), "word3")
    def test_rule12_27(self):
        self.assertEqual(pluralize(self.sixwordlist, 210, self.ARABIC), "word3")
    def test_rule12_28(self):
        self.assertEqual(pluralize(self.sixwordlist,  11, self.ARABIC), "word4")
    def test_rule12_29(self):
        self.assertEqual(pluralize(self.sixwordlist,  12, self.ARABIC), "word4")
    def test_rule12_30(self):
        self.assertEqual(pluralize(self.sixwordlist,  13, self.ARABIC), "word4")
    def test_rule12_31(self):
        self.assertEqual(pluralize(self.sixwordlist,  14, self.ARABIC), "word4")
    def test_rule12_32(self):
        self.assertEqual(pluralize(self.sixwordlist,  15, self.ARABIC), "word4")
    def test_rule12_33(self):
        self.assertEqual(pluralize(self.sixwordlist,  16, self.ARABIC), "word4")
    def test_rule12_34(self):
        self.assertEqual(pluralize(self.sixwordlist,  17, self.ARABIC), "word4")
    def test_rule12_35(self):
        self.assertEqual(pluralize(self.sixwordlist,  18, self.ARABIC), "word4")
    def test_rule12_36(self):
        self.assertEqual(pluralize(self.sixwordlist,  19, self.ARABIC), "word4")
    def test_rule12_37(self):
        self.assertEqual(pluralize(self.sixwordlist,  20, self.ARABIC), "word4")
    def test_rule12_38(self):
        self.assertEqual(pluralize(self.sixwordlist,  21, self.ARABIC), "word4")
    def test_rule12_39(self):
        self.assertEqual(pluralize(self.sixwordlist,  22, self.ARABIC), "word4")
    def test_rule12_40(self):
        self.assertEqual(pluralize(self.sixwordlist, 100, self.ARABIC), "word5")
    def test_rule12_41(self):
        self.assertEqual(pluralize(self.sixwordlist, 101, self.ARABIC), "word5")
    def test_rule12_42(self):
        self.assertEqual(pluralize(self.sixwordlist, 102, self.ARABIC), "word5")
    def test_rule12_43(self):
        self.assertEqual(pluralize(self.sixwordlist, 200, self.ARABIC), "word5")
    def test_rule12_44(self):
        self.assertEqual(pluralize(self.sixwordlist, 201, self.ARABIC), "word5")
    def test_rule12_45(self):
        self.assertEqual(pluralize(self.sixwordlist, 202, self.ARABIC), "word5")

    def test_rule15_1(self):
        self.assertEqual(pluralize(self.wordlist,   0, self.ICELANDIC), "words")
    def test_rule15_2(self):
        self.assertEqual(pluralize(self.wordlist,   1, self.ICELANDIC), "word")
    def test_rule15_3(self):
        self.assertEqual(pluralize(self.wordlist,   2, self.ICELANDIC), "words")
    def test_rule15_4(self):
        self.assertEqual(pluralize(self.wordlist,   3, self.ICELANDIC), "words")
    def test_rule15_5(self):
        self.assertEqual(pluralize(self.wordlist,   4, self.ICELANDIC), "words")
    def test_rule15_6(self):
        self.assertEqual(pluralize(self.wordlist,   5, self.ICELANDIC), "words")
    def test_rule15_7(self):
        self.assertEqual(pluralize(self.wordlist,   6, self.ICELANDIC), "words")
    def test_rule15_8(self):
        self.assertEqual(pluralize(self.wordlist,   7, self.ICELANDIC), "words")
    def test_rule15_9(self):
        self.assertEqual(pluralize(self.wordlist,  10, self.ICELANDIC), "words")
    def test_rule15_10(self):
        self.assertEqual(pluralize(self.wordlist,  11, self.ICELANDIC), "words")
    def test_rule15_11(self):
        self.assertEqual(pluralize(self.wordlist,  12, self.ICELANDIC), "words")
    def test_rule15_12(self):
        self.assertEqual(pluralize(self.wordlist,  20, self.ICELANDIC), "words")
    def test_rule15_13(self):
        self.assertEqual(pluralize(self.wordlist,  21, self.ICELANDIC), "word")
    def test_rule15_14(self):
        self.assertEqual(pluralize(self.wordlist,  22, self.ICELANDIC), "words")

class TestRule6(unittest.TestCase):
    """For rule 6, more coverage using the samples given by Mozilla"""
    
    def setUp(self):
        self.words = ("word0", "word1", "word2")

    def test_Form0(self):
        self.assertEqual(pluralize(self.words,   1, 6), "word0")
        self.assertEqual(pluralize(self.words,  21, 6), "word0")
        self.assertEqual(pluralize(self.words,  31, 6), "word0")
        self.assertEqual(pluralize(self.words,  41, 6), "word0")
        self.assertEqual(pluralize(self.words,  51, 6), "word0")
        self.assertEqual(pluralize(self.words,  61, 6), "word0")
        self.assertEqual(pluralize(self.words,  71, 6), "word0")
        self.assertEqual(pluralize(self.words,  81, 6), "word0")
        self.assertEqual(pluralize(self.words,  91, 6), "word0")
        self.assertEqual(pluralize(self.words, 101, 6), "word0")
        self.assertEqual(pluralize(self.words, 121, 6), "word0")
        self.assertEqual(pluralize(self.words, 131, 6), "word0")
        self.assertEqual(pluralize(self.words, 141, 6), "word0")
        self.assertEqual(pluralize(self.words, 151, 6), "word0")
        self.assertEqual(pluralize(self.words, 161, 6), "word0")
        self.assertEqual(pluralize(self.words, 171, 6), "word0")
        self.assertEqual(pluralize(self.words, 181, 6), "word0")
        self.assertEqual(pluralize(self.words, 191, 6), "word0")
        self.assertEqual(pluralize(self.words, 201, 6), "word0")
        self.assertEqual(pluralize(self.words, 221, 6), "word0")
        self.assertEqual(pluralize(self.words, 231, 6), "word0")
        self.assertEqual(pluralize(self.words, 241, 6), "word0")
        self.assertEqual(pluralize(self.words, 251, 6), "word0")
        self.assertEqual(pluralize(self.words, 261, 6), "word0")
        self.assertEqual(pluralize(self.words, 271, 6), "word0")
        self.assertEqual(pluralize(self.words, 281, 6), "word0")
        self.assertEqual(pluralize(self.words, 291, 6), "word0")

    def test_Form1(self):
        self.assertEqual(pluralize(self.words,   0, 6), "word1")
        self.assertEqual(pluralize(self.words,  10, 6), "word1")
        self.assertEqual(pluralize(self.words,  11, 6), "word1")
        self.assertEqual(pluralize(self.words,  12, 6), "word1")
        self.assertEqual(pluralize(self.words,  13, 6), "word1")
        self.assertEqual(pluralize(self.words,  14, 6), "word1")
        self.assertEqual(pluralize(self.words,  15, 6), "word1")
        self.assertEqual(pluralize(self.words,  16, 6), "word1")
        self.assertEqual(pluralize(self.words,  17, 6), "word1")
        self.assertEqual(pluralize(self.words,  18, 6), "word1")
        self.assertEqual(pluralize(self.words,  19, 6), "word1")
        self.assertEqual(pluralize(self.words,  20, 6), "word1")
        self.assertEqual(pluralize(self.words,  30, 6), "word1")
        self.assertEqual(pluralize(self.words,  40, 6), "word1")
        self.assertEqual(pluralize(self.words,  50, 6), "word1")
        self.assertEqual(pluralize(self.words,  60, 6), "word1")
        self.assertEqual(pluralize(self.words,  70, 6), "word1")
        self.assertEqual(pluralize(self.words,  80, 6), "word1")
        self.assertEqual(pluralize(self.words,  90, 6), "word1")
        self.assertEqual(pluralize(self.words, 100, 6), "word1")
        self.assertEqual(pluralize(self.words, 110, 6), "word1")
        self.assertEqual(pluralize(self.words, 111, 6), "word1")
        self.assertEqual(pluralize(self.words, 112, 6), "word1")
        self.assertEqual(pluralize(self.words, 113, 6), "word1")
        self.assertEqual(pluralize(self.words, 114, 6), "word1")
        self.assertEqual(pluralize(self.words, 115, 6), "word1")
        self.assertEqual(pluralize(self.words, 116, 6), "word1")
        self.assertEqual(pluralize(self.words, 117, 6), "word1")
        self.assertEqual(pluralize(self.words, 118, 6), "word1")
        self.assertEqual(pluralize(self.words, 119, 6), "word1")
        self.assertEqual(pluralize(self.words, 120, 6), "word1")
        self.assertEqual(pluralize(self.words, 130, 6), "word1")
        self.assertEqual(pluralize(self.words, 140, 6), "word1")
        self.assertEqual(pluralize(self.words, 150, 6), "word1")
        self.assertEqual(pluralize(self.words, 160, 6), "word1")
        self.assertEqual(pluralize(self.words, 170, 6), "word1")
        self.assertEqual(pluralize(self.words, 180, 6), "word1")
        self.assertEqual(pluralize(self.words, 190, 6), "word1")
        self.assertEqual(pluralize(self.words, 200, 6), "word1")
        self.assertEqual(pluralize(self.words, 210, 6), "word1")
        self.assertEqual(pluralize(self.words, 211, 6), "word1")
        self.assertEqual(pluralize(self.words, 212, 6), "word1")
        self.assertEqual(pluralize(self.words, 213, 6), "word1")
        self.assertEqual(pluralize(self.words, 214, 6), "word1")
        self.assertEqual(pluralize(self.words, 215, 6), "word1")
        self.assertEqual(pluralize(self.words, 216, 6), "word1")
        self.assertEqual(pluralize(self.words, 217, 6), "word1")
        self.assertEqual(pluralize(self.words, 218, 6), "word1")
        self.assertEqual(pluralize(self.words, 219, 6), "word1")
        self.assertEqual(pluralize(self.words, 220, 6), "word1")

    def test_Form2(self):
        self.assertEqual(pluralize(self.words,   2, 6), "word2")
        self.assertEqual(pluralize(self.words,   3, 6), "word2")
        self.assertEqual(pluralize(self.words,   4, 6), "word2")
        self.assertEqual(pluralize(self.words,   5, 6), "word2")
        self.assertEqual(pluralize(self.words,   6, 6), "word2")
        self.assertEqual(pluralize(self.words,   7, 6), "word2")
        self.assertEqual(pluralize(self.words,   8, 6), "word2")
        self.assertEqual(pluralize(self.words,   9, 6), "word2")
        self.assertEqual(pluralize(self.words,  22, 6), "word2")
        self.assertEqual(pluralize(self.words,  23, 6), "word2")
        self.assertEqual(pluralize(self.words,  24, 6), "word2")
        self.assertEqual(pluralize(self.words,  25, 6), "word2")
        self.assertEqual(pluralize(self.words,  26, 6), "word2")
        self.assertEqual(pluralize(self.words,  27, 6), "word2")
        self.assertEqual(pluralize(self.words,  28, 6), "word2")
        self.assertEqual(pluralize(self.words,  29, 6), "word2")
        self.assertEqual(pluralize(self.words,  32, 6), "word2")
        self.assertEqual(pluralize(self.words,  33, 6), "word2")
        self.assertEqual(pluralize(self.words,  34, 6), "word2")
        self.assertEqual(pluralize(self.words,  35, 6), "word2")
        self.assertEqual(pluralize(self.words,  36, 6), "word2")
        self.assertEqual(pluralize(self.words,  37, 6), "word2")
        self.assertEqual(pluralize(self.words,  38, 6), "word2")
        self.assertEqual(pluralize(self.words,  39, 6), "word2")
        self.assertEqual(pluralize(self.words,  42, 6), "word2")
        self.assertEqual(pluralize(self.words,  43, 6), "word2")
        self.assertEqual(pluralize(self.words,  44, 6), "word2")
        self.assertEqual(pluralize(self.words,  45, 6), "word2")
        self.assertEqual(pluralize(self.words,  46, 6), "word2")
        self.assertEqual(pluralize(self.words,  47, 6), "word2")
        self.assertEqual(pluralize(self.words,  48, 6), "word2")
        self.assertEqual(pluralize(self.words,  49, 6), "word2")
        self.assertEqual(pluralize(self.words,  52, 6), "word2")
        self.assertEqual(pluralize(self.words,  53, 6), "word2")
        self.assertEqual(pluralize(self.words,  54, 6), "word2")
        self.assertEqual(pluralize(self.words,  55, 6), "word2")
        self.assertEqual(pluralize(self.words,  56, 6), "word2")
        self.assertEqual(pluralize(self.words,  57, 6), "word2")
        self.assertEqual(pluralize(self.words,  58, 6), "word2")
        self.assertEqual(pluralize(self.words,  59, 6), "word2")
        self.assertEqual(pluralize(self.words,  62, 6), "word2")
        self.assertEqual(pluralize(self.words,  63, 6), "word2")
        self.assertEqual(pluralize(self.words,  64, 6), "word2")
        self.assertEqual(pluralize(self.words,  65, 6), "word2")
        self.assertEqual(pluralize(self.words,  66, 6), "word2")
        self.assertEqual(pluralize(self.words,  67, 6), "word2")
        self.assertEqual(pluralize(self.words,  68, 6), "word2")
        self.assertEqual(pluralize(self.words,  69, 6), "word2")
        self.assertEqual(pluralize(self.words,  72, 6), "word2")
        self.assertEqual(pluralize(self.words,  73, 6), "word2")

class TestRule7(unittest.TestCase):
    """For rule 7, more coverage using the samples given by Mozilla"""

    def test_Form0(self):
        words = ("word0", "word1", "word2")
        self.assertEqual(pluralize(words,   1, 7), "word0")
        self.assertEqual(pluralize(words,  21, 7), "word0")
        self.assertEqual(pluralize(words,  31, 7), "word0")
        self.assertEqual(pluralize(words,  41, 7), "word0")
        self.assertEqual(pluralize(words,  51, 7), "word0")
        self.assertEqual(pluralize(words,  61, 7), "word0")
        self.assertEqual(pluralize(words,  71, 7), "word0")
        self.assertEqual(pluralize(words,  81, 7), "word0")
        self.assertEqual(pluralize(words,  91, 7), "word0")
        self.assertEqual(pluralize(words, 101, 7), "word0")
        self.assertEqual(pluralize(words, 121, 7), "word0")
        self.assertEqual(pluralize(words, 131, 7), "word0")
        self.assertEqual(pluralize(words, 141, 7), "word0")
        self.assertEqual(pluralize(words, 151, 7), "word0")
        self.assertEqual(pluralize(words, 161, 7), "word0")
        self.assertEqual(pluralize(words, 171, 7), "word0")
        self.assertEqual(pluralize(words, 181, 7), "word0")
        self.assertEqual(pluralize(words, 191, 7), "word0")
        self.assertEqual(pluralize(words, 201, 7), "word0")
        self.assertEqual(pluralize(words, 221, 7), "word0")
        self.assertEqual(pluralize(words, 231, 7), "word0")
        self.assertEqual(pluralize(words, 241, 7), "word0")
        self.assertEqual(pluralize(words, 251, 7), "word0")
        self.assertEqual(pluralize(words, 261, 7), "word0")
        self.assertEqual(pluralize(words, 271, 7), "word0")
        self.assertEqual(pluralize(words, 281, 7), "word0")
        self.assertEqual(pluralize(words, 291, 7), "word0")

    def test_Form1(self):
        words = ("word0", "word1", "word2")
        self.assertEqual(pluralize(words,   2, 7), "word1")
        self.assertEqual(pluralize(words,   3, 7), "word1")
        self.assertEqual(pluralize(words,   4, 7), "word1")
        self.assertEqual(pluralize(words,  22, 7), "word1")
        self.assertEqual(pluralize(words,  23, 7), "word1")
        self.assertEqual(pluralize(words,  24, 7), "word1")
        self.assertEqual(pluralize(words,  32, 7), "word1")
        self.assertEqual(pluralize(words,  33, 7), "word1")
        self.assertEqual(pluralize(words,  34, 7), "word1")
        self.assertEqual(pluralize(words,  42, 7), "word1")
        self.assertEqual(pluralize(words,  43, 7), "word1")
        self.assertEqual(pluralize(words,  44, 7), "word1")
        self.assertEqual(pluralize(words,  52, 7), "word1")
        self.assertEqual(pluralize(words,  53, 7), "word1")
        self.assertEqual(pluralize(words,  54, 7), "word1")
        self.assertEqual(pluralize(words,  62, 7), "word1")
        self.assertEqual(pluralize(words,  63, 7), "word1")
        self.assertEqual(pluralize(words,  64, 7), "word1")
        self.assertEqual(pluralize(words,  72, 7), "word1")
        self.assertEqual(pluralize(words,  73, 7), "word1")
        self.assertEqual(pluralize(words,  74, 7), "word1")
        self.assertEqual(pluralize(words,  82, 7), "word1")
        self.assertEqual(pluralize(words,  83, 7), "word1")
        self.assertEqual(pluralize(words,  84, 7), "word1")
        self.assertEqual(pluralize(words,  92, 7), "word1")
        self.assertEqual(pluralize(words,  93, 7), "word1")
        self.assertEqual(pluralize(words,  94, 7), "word1")
        self.assertEqual(pluralize(words, 102, 7), "word1")
        self.assertEqual(pluralize(words, 103, 7), "word1")
        self.assertEqual(pluralize(words, 104, 7), "word1")
        self.assertEqual(pluralize(words, 122, 7), "word1")
        self.assertEqual(pluralize(words, 123, 7), "word1")
        self.assertEqual(pluralize(words, 124, 7), "word1")
        self.assertEqual(pluralize(words, 132, 7), "word1")
        self.assertEqual(pluralize(words, 133, 7), "word1")
        self.assertEqual(pluralize(words, 134, 7), "word1")
        self.assertEqual(pluralize(words, 142, 7), "word1")
        self.assertEqual(pluralize(words, 143, 7), "word1")
        self.assertEqual(pluralize(words, 144, 7), "word1")
        self.assertEqual(pluralize(words, 152, 7), "word1")
        self.assertEqual(pluralize(words, 153, 7), "word1")
        self.assertEqual(pluralize(words, 154, 7), "word1")
        self.assertEqual(pluralize(words, 162, 7), "word1")
        self.assertEqual(pluralize(words, 163, 7), "word1")
        self.assertEqual(pluralize(words, 164, 7), "word1")
        self.assertEqual(pluralize(words, 172, 7), "word1")
        self.assertEqual(pluralize(words, 173, 7), "word1")
        self.assertEqual(pluralize(words, 174, 7), "word1")
        self.assertEqual(pluralize(words, 182, 7), "word1")
        self.assertEqual(pluralize(words, 183, 7), "word1")

    def test_Form2(self):
        words = ("word0", "word1", "word2")
        self.assertEqual(pluralize(words,   0, 7), "word2")
        self.assertEqual(pluralize(words,   5, 7), "word2")
        self.assertEqual(pluralize(words,   6, 7), "word2")
        self.assertEqual(pluralize(words,   7, 7), "word2")
        self.assertEqual(pluralize(words,   8, 7), "word2")
        self.assertEqual(pluralize(words,   9, 7), "word2")
        self.assertEqual(pluralize(words,  10, 7), "word2")
        self.assertEqual(pluralize(words,  11, 7), "word2")
        self.assertEqual(pluralize(words,  12, 7), "word2")
        self.assertEqual(pluralize(words,  13, 7), "word2")
        self.assertEqual(pluralize(words,  14, 7), "word2")
        self.assertEqual(pluralize(words,  15, 7), "word2")
        self.assertEqual(pluralize(words,  16, 7), "word2")
        self.assertEqual(pluralize(words,  17, 7), "word2")
        self.assertEqual(pluralize(words,  18, 7), "word2")
        self.assertEqual(pluralize(words,  19, 7), "word2")
        self.assertEqual(pluralize(words,  20, 7), "word2")
        self.assertEqual(pluralize(words,  25, 7), "word2")
        self.assertEqual(pluralize(words,  26, 7), "word2")
        self.assertEqual(pluralize(words,  27, 7), "word2")
        self.assertEqual(pluralize(words,  28, 7), "word2")
        self.assertEqual(pluralize(words,  29, 7), "word2")
        self.assertEqual(pluralize(words,  30, 7), "word2")
        self.assertEqual(pluralize(words,  35, 7), "word2")
        self.assertEqual(pluralize(words,  36, 7), "word2")
        self.assertEqual(pluralize(words,  37, 7), "word2")
        self.assertEqual(pluralize(words,  38, 7), "word2")
        self.assertEqual(pluralize(words,  39, 7), "word2")
        self.assertEqual(pluralize(words,  40, 7), "word2")
        self.assertEqual(pluralize(words,  45, 7), "word2")
        self.assertEqual(pluralize(words,  46, 7), "word2")
        self.assertEqual(pluralize(words,  47, 7), "word2")
        self.assertEqual(pluralize(words,  48, 7), "word2")
        self.assertEqual(pluralize(words,  49, 7), "word2")
        self.assertEqual(pluralize(words,  50, 7), "word2")
        self.assertEqual(pluralize(words,  55, 7), "word2")
        self.assertEqual(pluralize(words,  56, 7), "word2")
        self.assertEqual(pluralize(words,  57, 7), "word2")
        self.assertEqual(pluralize(words,  58, 7), "word2")
        self.assertEqual(pluralize(words,  59, 7), "word2")
        self.assertEqual(pluralize(words,  60, 7), "word2")
        self.assertEqual(pluralize(words,  65, 7), "word2")
        self.assertEqual(pluralize(words,  66, 7), "word2")
        self.assertEqual(pluralize(words,  67, 7), "word2")
        self.assertEqual(pluralize(words,  68, 7), "word2")
        self.assertEqual(pluralize(words,  69, 7), "word2")
        self.assertEqual(pluralize(words,  70, 7), "word2")
        self.assertEqual(pluralize(words,  75, 7), "word2")
        self.assertEqual(pluralize(words,  76, 7), "word2")
        self.assertEqual(pluralize(words,  77, 7), "word2")

class TestRule9(unittest.TestCase):
    """For rule 9, more coverage using the samples given by Mozilla"""

    def test_Form0(self):
        words = ("word0", "word1", "word2")
        self.assertEqual(pluralize(words,   1, 9), "word0")

    def test_Form1(self):
        words = ("word0", "word1", "word2")
        self.assertEqual(pluralize(words,   2, 9), "word1")
        self.assertEqual(pluralize(words,   3, 9), "word1")
        self.assertEqual(pluralize(words,   4, 9), "word1")
        self.assertEqual(pluralize(words,  22, 9), "word1")
        self.assertEqual(pluralize(words,  23, 9), "word1")
        self.assertEqual(pluralize(words,  24, 9), "word1")
        self.assertEqual(pluralize(words, 102, 9), "word1")
        self.assertEqual(pluralize(words, 103, 9), "word1")
        self.assertEqual(pluralize(words, 104, 9), "word1")
        self.assertEqual(pluralize(words, 122, 9), "word1")
        self.assertEqual(pluralize(words, 123, 9), "word1")
        self.assertEqual(pluralize(words, 124, 9), "word1")

    def test_Form2(self):
        words = ("word0", "word1", "word2")
        self.assertEqual(pluralize(words,   0, 9), "word2")
        self.assertEqual(pluralize(words,   5, 9), "word2")
        self.assertEqual(pluralize(words,   6, 9), "word2")
        self.assertEqual(pluralize(words,   7, 9), "word2")
        self.assertEqual(pluralize(words,   8, 9), "word2")
        self.assertEqual(pluralize(words,   9, 9), "word2")
        self.assertEqual(pluralize(words,  10, 9), "word2")
        self.assertEqual(pluralize(words,  11, 9), "word2")
        self.assertEqual(pluralize(words,  12, 9), "word2")
        self.assertEqual(pluralize(words,  13, 9), "word2")
        self.assertEqual(pluralize(words,  14, 9), "word2")
        self.assertEqual(pluralize(words,  20, 9), "word2")
        self.assertEqual(pluralize(words,  21, 9), "word2")
        self.assertEqual(pluralize(words,  25, 9), "word2")
        self.assertEqual(pluralize(words,  26, 9), "word2")

class TestRule13(unittest.TestCase):
    """For rule 13, more coverage using the samples given by Mozilla"""

    def test_Form0(self):
        words = ("word0", "word1", "word2", "word3")
        self.assertEqual(pluralize(words,   1, 13), "word0")

    def test_Form1(self):
        words = ("word0", "word1", "word2", "word3")
        self.assertEqual(pluralize(words,   0, 13), "word1")
        self.assertEqual(pluralize(words,   2, 13), "word1")
        self.assertEqual(pluralize(words,   3, 13), "word1")
        self.assertEqual(pluralize(words,   4, 13), "word1")
        self.assertEqual(pluralize(words,   5, 13), "word1")
        self.assertEqual(pluralize(words,   6, 13), "word1")
        self.assertEqual(pluralize(words,   7, 13), "word1")
        self.assertEqual(pluralize(words,   8, 13), "word1")
        self.assertEqual(pluralize(words,   9, 13), "word1")
        self.assertEqual(pluralize(words,  10, 13), "word1")
        self.assertEqual(pluralize(words, 101, 13), "word1")
        self.assertEqual(pluralize(words, 102, 13), "word1")
        self.assertEqual(pluralize(words, 103, 13), "word1")
        self.assertEqual(pluralize(words, 104, 13), "word1")
        self.assertEqual(pluralize(words, 105, 13), "word1")
        self.assertEqual(pluralize(words, 106, 13), "word1")
        self.assertEqual(pluralize(words, 107, 13), "word1")
        self.assertEqual(pluralize(words, 108, 13), "word1")
        self.assertEqual(pluralize(words, 109, 13), "word1")
        self.assertEqual(pluralize(words, 110, 13), "word1")
        self.assertEqual(pluralize(words, 201, 13), "word1")
        self.assertEqual(pluralize(words, 202, 13), "word1")
        self.assertEqual(pluralize(words, 203, 13), "word1")
        self.assertEqual(pluralize(words, 204, 13), "word1")
        self.assertEqual(pluralize(words, 205, 13), "word1")
        self.assertEqual(pluralize(words, 206, 13), "word1")
        self.assertEqual(pluralize(words, 207, 13), "word1")
        self.assertEqual(pluralize(words, 208, 13), "word1")
        self.assertEqual(pluralize(words, 209, 13), "word1")
        self.assertEqual(pluralize(words, 210, 13), "word1")

    def test_Form2(self):
        words = ("word0", "word1", "word2", "word3")
        self.assertEqual(pluralize(words,  11, 13), "word2")
        self.assertEqual(pluralize(words,  12, 13), "word2")
        self.assertEqual(pluralize(words,  13, 13), "word2")
        self.assertEqual(pluralize(words,  14, 13), "word2")
        self.assertEqual(pluralize(words,  15, 13), "word2")
        self.assertEqual(pluralize(words,  16, 13), "word2")
        self.assertEqual(pluralize(words,  17, 13), "word2")
        self.assertEqual(pluralize(words,  18, 13), "word2")
        self.assertEqual(pluralize(words,  19, 13), "word2")
        self.assertEqual(pluralize(words, 111, 13), "word2")
        self.assertEqual(pluralize(words, 112, 13), "word2")
        self.assertEqual(pluralize(words, 113, 13), "word2")
        self.assertEqual(pluralize(words, 114, 13), "word2")
        self.assertEqual(pluralize(words, 115, 13), "word2")
        self.assertEqual(pluralize(words, 116, 13), "word2")
        self.assertEqual(pluralize(words, 117, 13), "word2")
        self.assertEqual(pluralize(words, 118, 13), "word2")
        self.assertEqual(pluralize(words, 119, 13), "word2")
        self.assertEqual(pluralize(words, 211, 13), "word2")
        self.assertEqual(pluralize(words, 212, 13), "word2")
        self.assertEqual(pluralize(words, 213, 13), "word2")
        self.assertEqual(pluralize(words, 214, 13), "word2")
        self.assertEqual(pluralize(words, 215, 13), "word2")
        self.assertEqual(pluralize(words, 216, 13), "word2")
        self.assertEqual(pluralize(words, 217, 13), "word2")
        self.assertEqual(pluralize(words, 218, 13), "word2")
        self.assertEqual(pluralize(words, 219, 13), "word2")

    def test_Form3(self):
        words = ("word0", "word1", "word2", "word3")
        self.assertEqual(pluralize(words,  20, 13), "word3")
        self.assertEqual(pluralize(words,  21, 13), "word3")
        self.assertEqual(pluralize(words,  22, 13), "word3")
        self.assertEqual(pluralize(words,  23, 13), "word3")
        self.assertEqual(pluralize(words,  24, 13), "word3")
        self.assertEqual(pluralize(words,  25, 13), "word3")
        self.assertEqual(pluralize(words,  26, 13), "word3")
        self.assertEqual(pluralize(words,  27, 13), "word3")
        self.assertEqual(pluralize(words,  28, 13), "word3")
        self.assertEqual(pluralize(words,  29, 13), "word3")
        self.assertEqual(pluralize(words,  30, 13), "word3")
        self.assertEqual(pluralize(words,  31, 13), "word3")
        self.assertEqual(pluralize(words,  32, 13), "word3")
        self.assertEqual(pluralize(words,  33, 13), "word3")
        self.assertEqual(pluralize(words,  34, 13), "word3")
        self.assertEqual(pluralize(words,  35, 13), "word3")
        self.assertEqual(pluralize(words,  36, 13), "word3")
        self.assertEqual(pluralize(words,  37, 13), "word3")
        self.assertEqual(pluralize(words,  38, 13), "word3")
        self.assertEqual(pluralize(words,  39, 13), "word3")
        self.assertEqual(pluralize(words,  40, 13), "word3")
        self.assertEqual(pluralize(words,  41, 13), "word3")
        self.assertEqual(pluralize(words,  42, 13), "word3")
        self.assertEqual(pluralize(words,  43, 13), "word3")
        self.assertEqual(pluralize(words,  44, 13), "word3")
        self.assertEqual(pluralize(words,  45, 13), "word3")
        self.assertEqual(pluralize(words,  46, 13), "word3")
        self.assertEqual(pluralize(words,  47, 13), "word3")
        self.assertEqual(pluralize(words,  48, 13), "word3")
        self.assertEqual(pluralize(words,  49, 13), "word3")
        self.assertEqual(pluralize(words,  50, 13), "word3")
        self.assertEqual(pluralize(words,  51, 13), "word3")
        self.assertEqual(pluralize(words,  52, 13), "word3")
        self.assertEqual(pluralize(words,  53, 13), "word3")
        self.assertEqual(pluralize(words,  54, 13), "word3")
        self.assertEqual(pluralize(words,  55, 13), "word3")
        self.assertEqual(pluralize(words,  56, 13), "word3")
        self.assertEqual(pluralize(words,  57, 13), "word3")
        self.assertEqual(pluralize(words,  58, 13), "word3")
        self.assertEqual(pluralize(words,  59, 13), "word3")
        self.assertEqual(pluralize(words,  60, 13), "word3")
        self.assertEqual(pluralize(words,  61, 13), "word3")
        self.assertEqual(pluralize(words,  62, 13), "word3")
        self.assertEqual(pluralize(words,  63, 13), "word3")
        self.assertEqual(pluralize(words,  64, 13), "word3")
        self.assertEqual(pluralize(words,  65, 13), "word3")
        self.assertEqual(pluralize(words,  66, 13), "word3")
        self.assertEqual(pluralize(words,  67, 13), "word3")
        self.assertEqual(pluralize(words,  68, 13), "word3")
        self.assertEqual(pluralize(words,  69, 13), "word3")

class TestRule14(unittest.TestCase):
    """For rule 14, more coverage using the samples given by Mozilla"""

    def test_Form0(self):
        words = ("word0", "word1", "word2")
        self.assertEqual(pluralize(words,   1, 14), "word0")
        self.assertEqual(pluralize(words,  11, 14), "word0")
        self.assertEqual(pluralize(words,  21, 14), "word0")
        self.assertEqual(pluralize(words,  31, 14), "word0")
        self.assertEqual(pluralize(words,  41, 14), "word0")
        self.assertEqual(pluralize(words,  51, 14), "word0")
        self.assertEqual(pluralize(words,  61, 14), "word0")
        self.assertEqual(pluralize(words,  71, 14), "word0")
        self.assertEqual(pluralize(words,  81, 14), "word0")
        self.assertEqual(pluralize(words,  91, 14), "word0")
        self.assertEqual(pluralize(words, 101, 14), "word0")
        self.assertEqual(pluralize(words, 111, 14), "word0")
        self.assertEqual(pluralize(words, 121, 14), "word0")
        self.assertEqual(pluralize(words, 131, 14), "word0")
        self.assertEqual(pluralize(words, 141, 14), "word0")
        self.assertEqual(pluralize(words, 151, 14), "word0")
        self.assertEqual(pluralize(words, 161, 14), "word0")
        self.assertEqual(pluralize(words, 171, 14), "word0")
        self.assertEqual(pluralize(words, 181, 14), "word0")
        self.assertEqual(pluralize(words, 191, 14), "word0")
        self.assertEqual(pluralize(words, 201, 14), "word0")
        self.assertEqual(pluralize(words, 211, 14), "word0")
        self.assertEqual(pluralize(words, 221, 14), "word0")
        self.assertEqual(pluralize(words, 231, 14), "word0")
        self.assertEqual(pluralize(words, 241, 14), "word0")
        self.assertEqual(pluralize(words, 251, 14), "word0")
        self.assertEqual(pluralize(words, 261, 14), "word0")
        self.assertEqual(pluralize(words, 271, 14), "word0")
        self.assertEqual(pluralize(words, 281, 14), "word0")
        self.assertEqual(pluralize(words, 291, 14), "word0")

    def test_Form1(self):
        words = ("word0", "word1", "word2")
        self.assertEqual(pluralize(words,   2, 14), "word1")
        self.assertEqual(pluralize(words,  12, 14), "word1")
        self.assertEqual(pluralize(words,  22, 14), "word1")
        self.assertEqual(pluralize(words,  32, 14), "word1")
        self.assertEqual(pluralize(words,  42, 14), "word1")
        self.assertEqual(pluralize(words,  52, 14), "word1")
        self.assertEqual(pluralize(words,  62, 14), "word1")
        self.assertEqual(pluralize(words,  72, 14), "word1")
        self.assertEqual(pluralize(words,  82, 14), "word1")
        self.assertEqual(pluralize(words,  92, 14), "word1")
        self.assertEqual(pluralize(words, 102, 14), "word1")
        self.assertEqual(pluralize(words, 112, 14), "word1")
        self.assertEqual(pluralize(words, 122, 14), "word1")
        self.assertEqual(pluralize(words, 132, 14), "word1")
        self.assertEqual(pluralize(words, 142, 14), "word1")
        self.assertEqual(pluralize(words, 152, 14), "word1")
        self.assertEqual(pluralize(words, 162, 14), "word1")
        self.assertEqual(pluralize(words, 172, 14), "word1")
        self.assertEqual(pluralize(words, 182, 14), "word1")
        self.assertEqual(pluralize(words, 192, 14), "word1")
        self.assertEqual(pluralize(words, 202, 14), "word1")
        self.assertEqual(pluralize(words, 212, 14), "word1")
        self.assertEqual(pluralize(words, 222, 14), "word1")
        self.assertEqual(pluralize(words, 232, 14), "word1")
        self.assertEqual(pluralize(words, 242, 14), "word1")
        self.assertEqual(pluralize(words, 252, 14), "word1")
        self.assertEqual(pluralize(words, 262, 14), "word1")
        self.assertEqual(pluralize(words, 272, 14), "word1")
        self.assertEqual(pluralize(words, 282, 14), "word1")
        self.assertEqual(pluralize(words, 292, 14), "word1")

    def test_Form2(self):
        words = ("word0", "word1", "word2")
        self.assertEqual(pluralize(words,   0, 14), "word2")
        self.assertEqual(pluralize(words,   3, 14), "word2")
        self.assertEqual(pluralize(words,   4, 14), "word2")
        self.assertEqual(pluralize(words,   5, 14), "word2")
        self.assertEqual(pluralize(words,   6, 14), "word2")
        self.assertEqual(pluralize(words,   7, 14), "word2")
        self.assertEqual(pluralize(words,   8, 14), "word2")
        self.assertEqual(pluralize(words,   9, 14), "word2")
        self.assertEqual(pluralize(words,  10, 14), "word2")
        self.assertEqual(pluralize(words,  13, 14), "word2")
        self.assertEqual(pluralize(words,  14, 14), "word2")
        self.assertEqual(pluralize(words,  15, 14), "word2")
        self.assertEqual(pluralize(words,  16, 14), "word2")
        self.assertEqual(pluralize(words,  20, 14), "word2")
        self.assertEqual(pluralize(words,  23, 14), "word2")
        self.assertEqual(pluralize(words,  24, 14), "word2")
        self.assertEqual(pluralize(words,  25, 14), "word2")
        self.assertEqual(pluralize(words,  26, 14), "word2")

class TestExplain(unittest.TestCase):
    
    def test_failure(self):
        self.assertRaises(RuleError, explain, 500)

    def test_1form(self):
    # expect rule 0 to have 1 form
        self.assertEqual(len(explain(0)), 1)
    
    # expect rule 1, 2, 15 to have 2 forms
    def test_2forms_1(self):
        self.assertEqual(len(explain(1)), 2)
    def test_2forms_2(self):
        self.assertEqual(len(explain(2)), 2)
    def test_2forms_15(self):
        self.assertEqual(len(explain(15)), 2)

    # expect rule 3, 5-9, 14 to have 3 forms
    def test_3forms_3(self):
        self.assertEqual(len(explain(3)), 3)
    def test_3forms_5(self):
        self.assertEqual(len(explain(5)), 3)
    def test_3forms_6(self):
        self.assertEqual(len(explain(6)), 3)
    def test_3forms_7(self):
        self.assertEqual(len(explain(7)), 3)
    def test_3forms_8(self):
        self.assertEqual(len(explain(8)), 3)
    def test_3forms_9(self):
        self.assertEqual(len(explain(9)), 3)
    def test_3forms_14(self):
        self.assertEqual(len(explain(14)), 3)
    
    # expect rule 4, 10, 13 to have 4 forms
    def test_4forms_4(self):
        self.assertEqual(len(explain(4)), 4)
    def test_4forms_10(self):
        self.assertEqual(len(explain(10)), 4)
    def test_4forms_13(self):
        self.assertEqual(len(explain(13)), 4)
    
    def test_5forms(self):
        # expect rule 11 to have 5 forms
        self.assertEqual(len(explain(11)), 5)
    
    def test_6forms(self):
        # expect rule 12 to have 6 forms
        self.assertEqual(len(explain(12)), 6)

class TestRuleFor(unittest.TestCase):

    def test_basic_1(self):
        self.assertEqual(rulefor('en'), 1)
    def test_basic_2(self):
        self.assertEqual(rulefor('EN'), 1)
    def test_basic_3(self):
        self.assertEqual(rulefor('lt'), 6)
    def test_basic_4(self):
        self.assertEqual(rulefor('is'), 15)
    def test_basic_5(self):
        self.assertEqual(rulefor('klingon'), None)

if __name__ == '__main__':
    unittest.main()