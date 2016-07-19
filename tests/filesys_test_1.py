##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
from testlib import *

from auxly.filesys import makedirs, delete, is_empty, copy

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(unittest.TestCase):

    def test_makedirs_1(test):
        path = "foo/bar"
        test.assertFalse(os.path.exists(path))
        test.assertTrue(makedirs(path))
        test.assertTrue(os.path.exists(path))
        test.assertTrue(os.path.isdir(path))
        test.assertTrue(is_empty(path))
        test.assertTrue(delete(path))
        test.assertFalse(os.path.exists(path))

    def test_makedirs_2(test):
        path1 = "../foo"
        path2 = "../bar"
        test.assertFalse(os.path.exists(path1))
        test.assertTrue(makedirs(path1))
        test.assertTrue(os.path.exists(path1))
        test.assertTrue(os.path.isdir(path1))
        test.assertTrue(is_empty(path1))
        test.assertTrue(copy(path1, path2))
        test.assertTrue(delete(path1))
        test.assertTrue(delete(path2))
        test.assertFalse(os.path.exists(path1))
        test.assertFalse(os.path.exists(path2))

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()
