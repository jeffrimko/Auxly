##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
from testlib import *

from auxly.shell import has, listout, iterout, start

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):
    def test_listout_1(test):
        if has("ls"):
            ls = sorted(listout("ls"))
            py = sorted(os.listdir("."))
            test.assertEqual(ls, py)

    def test_iterout_1(test):
        if has("ls"):
            ls = sorted(iterout("ls"))
            py = sorted(os.listdir("."))
            test.assertEqual(ls, py)

    def test_start_1(test):
        if has("ls"):
            p = start("ls")
            while True:
                result = p.exitcode()
                if result != None:
                    break
            test.assertEqual(0, result)

    def test_start_2(test):
        if has("ls"):
            p = start("ls")
            result = p.wait()
            test.assertEqual(0, result)

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()
