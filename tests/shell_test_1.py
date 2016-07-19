##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
from testlib import *

from auxly.shell import has, listout, iterout

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(unittest.TestCase):

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

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()
