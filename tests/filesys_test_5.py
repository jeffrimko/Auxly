##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from testlib import *

from auxly.filesys import Path

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):

    def test_path_1(test):
        """Basic Path usage."""
        path = FNAME[0]
        fwrite(path, TEXT[0])
        dir_ = op.abspath(".")
        p = Path(path)
        test.assertTrue(p.exists())
        test.assertTrue(p.isfile())
        test.assertFalse(p.isdir())
        test.assertEqual(dir_, p.parent)
        test.assertEqual(FNAME[0], p.name)

    def test_path_2(test):
        """Basic Path usage."""
        p = Path(DIR[0], FNAME[0])
        test.assertFalse(p.exists())
        test.assertFalse(p.isfile())
        test.assertFalse(p.isdir())
        test.assertEqual(op.abspath(op.join(DIR[0], FNAME[0])), p)
        test.assertEqual(FNAME[0], p.name)

    def test_path_3(test):
        """Basic Path usage."""
        p = Path("not_a_real_dir")
        test.assertFalse(p.exists())
        test.assertFalse(p.isfile())
        test.assertFalse(p.isdir())
        test.assertTrue(None == p.created())
        test.assertTrue(None == p.modified())
        test.assertTrue(None == p.size())
        test.assertTrue(None == p.isempty())
        test.assertTrue(None == p.isempty())
        test.assertTrue("not_a_real_dir" == p.name)

    def test_path_4(test):
        """Basic Path usage."""
        with test.assertRaises(TypeError):
            p = Path()

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()
