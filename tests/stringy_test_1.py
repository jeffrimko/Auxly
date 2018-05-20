##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
from testlib import *

from auxly.stringy import subidx, randomize

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):
    def test_subidx_1(test):
        test.assertEqual('xello', subidx("hello", 0, "x"))
        test.assertEqual('heLlo', subidx("hello", 2, "L"))
        test.assertEqual('hiyllo', subidx("hello", 1, "iy"))
        test.assertEqual('hello', subidx("hello", 10, "x"))
        test.assertEqual('ello', subidx("hello", 0, ""))

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
