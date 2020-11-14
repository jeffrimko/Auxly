##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from testlib import *

from auxly import AuxlyError, throw
from auxly.filesys import move

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):
    def test_throw_1(test):
        test.assertFalse(move("fake1.txt", "fake2.txt"))
        with test.assertRaises(AuxlyError):
            move("fake1.txt", "fake2.txt") or throw()

    def test_throw_2(test):
        test.assertFalse(move("fake1.txt", "fake2.txt"))
        with test.assertRaises(AuxlyError) as cm:
            move("fake1.txt", "fake2.txt") or throw("error message")
        test.assertEqual("error message", str(cm.exception))

    def test_throw_3(test):
        test.assertFalse(move("fake1.txt", "fake2.txt"))
        with test.assertRaises(AssertionError):
            move("fake1.txt", "fake2.txt") or throw(AssertionError)

    def test_throw_4(test):
        test.assertFalse(move("fake1.txt", "fake2.txt"))
        with test.assertRaises(ValueError) as cm:
            move("fake1.txt", "fake2.txt") or throw(ValueError, "something went wrong")
        test.assertEqual("something went wrong", str(cm.exception))

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()
