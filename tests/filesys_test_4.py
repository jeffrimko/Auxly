##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from testlib import *

import auxly
from auxly.filesys import move, makedirs, isempty

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):
    def test_move_1(test):
        """Regression check for release `0.3.0`; bug fix for deleting
        file if src and dst are the same."""
        path = FNAME[0]
        test.assertFalse(move(path, path))
        fwrite(path, TEXT[0])
        test.assertTrue(op.isfile(path))
        test.assertTrue(move(path, path))
        test.assertTrue(op.isfile(path))

    def test_move_2(test):
        """Move file to dir/file, dir does not previously exist."""
        path0 = FNAME[0]
        path1 = op.join(DIR[0], FNAME[0])
        fwrite(path0, TEXT[0])
        test.assertTrue(op.isfile(path0))
        test.assertFalse(op.isdir(DIR[0]))
        test.assertFalse(op.isfile(path1))
        test.assertTrue(move(path0, path1))
        test.assertFalse(op.isfile(path0))
        test.assertTrue(op.isdir(DIR[0]))
        test.assertTrue(op.isfile(path1))

    def test_move_2(test):
        """Move file to dir/file, overwrite existing file."""
        path0 = FNAME[0]
        path1 = op.join(DIR[0], FNAME[0])
        fwrite(path0, TEXT[0])
        fwrite(path1, TEXT[1])
        test.assertTrue(op.isfile(path0))
        test.assertTrue(op.isdir(DIR[0]))
        test.assertTrue(op.isfile(path1))
        test.assertTrue(move(path0, path1))
        test.assertTrue(TEXT[0] == fread(path1))
        test.assertFalse(op.isfile(path0))
        test.assertTrue(op.isdir(DIR[0]))
        test.assertTrue(op.isfile(path1))

    def test_move_3(test):
        """Move file to dir/file fails due to overwrite flag."""
        path0 = FNAME[0]
        path1 = op.join(DIR[0], FNAME[0])
        fwrite(path0, TEXT[0])
        fwrite(path1, TEXT[1])
        test.assertTrue(op.isfile(path0))
        test.assertTrue(op.isdir(DIR[0]))
        test.assertTrue(op.isfile(path1))
        test.assertFalse(move(path0, path1, overwrite=False))
        test.assertTrue(TEXT[0] == fread(path0))
        test.assertTrue(TEXT[1] == fread(path1))
        test.assertTrue(op.isfile(path0))
        test.assertTrue(op.isdir(DIR[0]))
        test.assertTrue(op.isfile(path1))

    def test_move_4(test):
        """Move file to dir."""
        path0 = FNAME[0]
        path1 = DIR[0]
        fpath1 = op.join(path1, path0)
        fwrite(path0, TEXT[0])
        test.assertTrue(makedirs(path1))
        test.assertTrue(op.isfile(path0))
        test.assertTrue(op.isdir(path1))
        test.assertTrue(move(path0, path1))
        test.assertTrue(TEXT[0] == fread(fpath1))
        test.assertFalse(op.isfile(path0))
        test.assertTrue(op.isdir(DIR[0]))
        test.assertTrue(op.isfile(fpath1))

    def test_move_5(test):
        """Copy dir to dir using relative src path."""
        test.assertTrue(makedirs(op.join(DIR[0], DIR[1])))
        test.assertTrue(makedirs(op.join(DIR[2])))
        test.assertFalse(op.isdir(DIR[1]))
        auxly.cwd(DIR[0])
        test.assertTrue(op.isdir(DIR[1]))
        path0 = op.join("..", DIR[2])
        path1 = DIR[1]
        tpath = op.join(DIR[1], DIR[2])
        test.assertFalse(op.isdir(tpath))
        test.assertTrue(move(path0, path1))
        test.assertFalse(op.isdir(path0))
        test.assertTrue(op.isdir(tpath))

    def test_move_6(test):
        """Move dir to dir using relative dst path."""
        test.assertTrue(makedirs(op.join(DIR[0], DIR[1])))
        auxly.cwd(DIR[0])
        test.assertTrue(op.isdir(DIR[1]))
        path0 = DIR[1]
        path1 = ".."
        tpath = op.join("..", DIR[1])
        test.assertFalse(op.isdir(tpath))
        test.assertTrue(move(path0, path1))
        test.assertFalse(op.isdir(path0))
        test.assertTrue(op.isdir(tpath))

    def test_move_7(test):
        """Move dir to dir that does not exist."""
        path0 = DIR[0]
        path1 = DIR[1]
        test.assertTrue(makedirs(path0))
        test.assertFalse(op.isdir(path1))
        test.assertTrue(move(path0, path1))
        test.assertFalse(op.isdir(path0))
        test.assertTrue(op.isdir(path1))
        test.assertTrue(isempty(path1))

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()
