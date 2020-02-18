##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
from testlib import *

from auxly import trycatch

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

VAL = 0

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):

    def test_trycatch_1(test):
        global VAL
        VAL = 0
        trycatch(goodfunc)(1)
        test.assertEqual(1, VAL)

    def test_trycatch_2(test):
        global VAL
        VAL = 0
        trycatch(badfunc)(1)
        test.assertEqual(0, VAL)

    def test_trycatch_3(test):
        global VAL
        VAL = 0
        trycatch(badfunc, oncatch=lambda: goodfunc(2))(1)
        test.assertEqual(2, VAL)

    def test_trycatch_4(test):
        global VAL
        VAL = 0
        with test.assertRaises(UnboundLocalError):
            trycatch(badfunc, rethrow=True)(1)
        test.assertEqual(0, VAL)

    def test_trycatch_5(test):
        vals = [1,2]
        with test.assertRaises(IndexError):
            trycatch(lambda: vals[100], rethrow=True)()

    def test_trycatch_6(test):
        vals = [1,2]
        result = trycatch(lambda: vals[100], oncatch=lambda: 123)()
        test.assertEqual(123, result)

    def test_trycatch_7(test):
        vals = [1,2]
        result = trycatch(lambda: vals[1], oncatch=lambda: 123)()
        test.assertEqual(2, result)

    def test_trycatch_8(test):
        vals = [1,2]
        result = None
        with test.assertRaises(IndexError):
            result = trycatch(lambda: vals[100], oncatch=lambda: 123, rethrow=True)()
        test.assertEqual(None, result)

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def goodfunc(a):
    global VAL
    VAL += a

def badfunc(a):
    global VAL
    x += 1
    VAL += a

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()
