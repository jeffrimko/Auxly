##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
from testlib import *

from auxly import callstop

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

VAL = 0

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):

    def test_callstop_1(test):
        global VAL
        VAL = 0
        call = callstop(increment)
        for _ in range(10):
            call(2)
        test.assertEqual(2, VAL)

    def test_callstop_2(test):
        global VAL
        VAL = 0
        call = callstop(increment, limit=4)
        for _ in range(10):
            call(1)
        test.assertEqual(4, VAL)

    def test_callstop_3(test):
        global VAL
        VAL = 0
        call = callstop(increment, limit=12)
        for _ in range(10):
            call(1)
        test.assertEqual(10, VAL)

    def test_callstop_4(test):
        global VAL
        VAL = 0
        for _ in range(10):
            incstop(1)
        test.assertEqual(4, VAL)

    def test_callstop_5(test):
        global VAL
        VAL = 0
        for _ in range(10):
            incstop(1)
        # Should not run at all due to previous test hitting limit.
        test.assertEqual(0, VAL)

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def increment(a):
    global VAL
    VAL += a

@callstop(limit=4)
def incstop(a):
    global VAL
    VAL += a

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()
