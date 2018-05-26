##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
from testlib import *

from auxly.stringy import subat, randomize

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):
    def test_subat_1(test):
        test.assertEqual('xello', subat("hello", 0, "x"))
        test.assertEqual('heLlo', subat("hello", 2, "L"))
        test.assertEqual('hiyllo', subat("hello", 1, "iy"))
        test.assertEqual('hello', subat("hello", 10, "x"))
        test.assertEqual('ello', subat("hello", 0, ""))

    def test_randomized_1(test):
        test.assertEqual(6, len(randomize()))
        test.assertEqual(6, len(randomize(choices="aeiou")))
        test.assertEqual(6, len(randomize(choices=["a", "e", "i", "o", "u"])))
        test.assertEqual(10, len(randomize(10)))

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()
