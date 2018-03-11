##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from testlib import *

from auxly import throw
from auxly.filesys import move

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):
    def test_throw_1(test):
        test.assertFalse(move("fake1.txt", "fake2.txt"))
        with test.assertRaises(Exception):
            move("fake1.txt", "fake2.txt") or throw()

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()
