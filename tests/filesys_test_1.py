##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os.path as op
from testlib import *

from auxly.filesys import makedirs, delete, isempty, copy

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(unittest.TestCase):

    def test_makedirs_1(test):
        path = "foo/bar"
        test.assertFalse(op.exists(path))
        test.assertTrue(makedirs(path))
        test.assertTrue(op.exists(path))
        test.assertTrue(op.isdir(path))
        test.assertTrue(isempty(path))
        test.assertTrue(delete(path))
        test.assertFalse(op.exists(path))
        test.assertTrue(delete(path.split("/")[0]))

    def test_makedirs_2(test):
        path1 = "../foo"
        path2 = "../bar"
        test.assertFalse(op.exists(path1))
        test.assertTrue(makedirs(path1))
        test.assertTrue(op.exists(path1))
        test.assertTrue(op.isdir(path1))
        test.assertTrue(isempty(path1))
        test.assertTrue(copy(path1, path2))
        test.assertTrue(delete(path1))
        test.assertTrue(delete(path2))
        test.assertFalse(op.exists(path1))
        test.assertFalse(op.exists(path2))

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()
