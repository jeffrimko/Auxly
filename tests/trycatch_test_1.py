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
