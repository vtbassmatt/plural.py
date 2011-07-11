import unittest
from plural import _endsin, endsin1, endsin0, endsin11, endsinanyof, strrange

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
    
    def test_strings(self):
        self.assertTrue(_endsin(2, '2'))
    
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

if __name__ == '__main__':
    unittest.main()