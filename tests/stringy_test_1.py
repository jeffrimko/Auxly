##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
from testlib import *

from auxly.stringy import subat, randomize, between, remove, subtract

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

    def test_between_1(test):
        test.assertEqual("hello", between("xhellox", "x", "x"))
        test.assertEqual("hello", between("xhelloxx", "x", "x"))
        test.assertEqual("hello", between(" hello!", " ", "!"))
        test.assertEqual("hello", between("abc hello!xyz", " ", "!"))
        test.assertEqual("hello", between("abc hello!xyz", "abc ", "!xyz"))
        test.assertEqual("hello", between("aaaabc hello!xyzzz", "abc ", "!xyz"))
        test.assertEqual("hello", between("hello", "not_there", "not_there"))
        test.assertEqual("hello", between("hello there", "", " there"))
        test.assertEqual("hello", between("hello there", "", " "))
        test.assertEqual("hello", between("hello", "", "not_there"))
        test.assertEqual("hello", between("hello", "", "aeiou"))
        test.assertEqual("hello", between("hello", "", ""))
        test.assertEqual("hello", between("xhello", "x", ""))
        test.assertEqual("hello", between("helloxworld", "", "x"))
        test.assertEqual("hello", between("lhello", "l", ""))
        test.assertEqual("hello", between("hello!!!world", "", "!"))

    def test_remove_1(test):
        test.assertEqual("hello world", remove("hello world!", "!"))
        test.assertEqual("hello world", remove("hello world!", ["!"]))
        test.assertEqual("abc", remove("abcdef", "def"))
        test.assertEqual("aaa", remove(" a a a ", " "))
        test.assertEqual("ab", remove("aaab", "aa"))
        test.assertEqual("abcdef", remove("abcdef", "acf"))
        test.assertEqual("bcf", remove("abdcef", list("ade")))

    def test_subtract_1(test):
        test.assertEqual("hello", subtract("hello.txt", ".txt"))
        test.assertEqual("hello.txt", subtract("hello.txt", "xyz"))
        test.assertEqual("", subtract("abc", "abc"))
        test.assertEqual("abc", subtract("abc", "a"))

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()
