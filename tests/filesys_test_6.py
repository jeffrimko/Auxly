##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from testlib import *

from auxly.filesys import File

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):
    def test_file_1(test):
        """Basic File usage."""
        p = FNAME[0]
        f = File(p)
        test.assertFalse(f.exists())
        test.assertTrue(f.write("hello"))
        test.assertTrue(f.append(" world"))
        test.assertTrue(f.exists())
        test.assertEqual("hello world", f.read())
        test.assertEqual("5eb63bbbe01eeed093cb22bb8f5acdc3", f.checksum())

    def test_file_2(test):
        """Basic File usage."""
        p = FNAME[0]
        f = File(p)
        test.assertFalse(f.exists())
        test.assertTrue(f.write("hello"))
        test.assertTrue(f.write("world"))
        test.assertEqual("world", f.read())
        test.assertFalse(f.isempty())
        test.assertTrue(f.empty())
        test.assertEqual("", f.read())
        test.assertTrue(f.isempty())

    def test_file_3(test):
        """Basic File usage."""
        p = FNAME[0]
        f = File(p)
        test.assertFalse(f.exists())
        test.assertTrue(f.write(123))
        test.assertEqual("123", f.read())

    def test_file_4(test):
        """Basic File usage."""
        p = FNAME[0]
        f = File(p)
        test.assertFalse(f.exists())
        test.assertTrue(f.writeline("hello"))
        test.assertEqual("hello" + os.linesep, f.read())

    def test_file_5(test):
        """Basic File usage."""
        p = FNAME[0]
        f = File(p)
        test.assertFalse(f.exists())
        test.assertTrue(f.writeline("hello"))
        test.assertTrue(f.append("world"))
        test.assertEqual("hello" + os.linesep + "world", f.read())

    def test_file_6(test):
        """Basic File usage."""
        p = FNAME[0]
        f = File(p)
        test.assertFalse(f.exists())
        test.assertTrue(f.writeline("hello"))
        test.assertTrue(f.appendline("world"))
        test.assertEqual("hello" + os.linesep + "world" + os.linesep, f.read())

    def test_file_7(test):
        """Basic File usage."""
        f = File(DIR[0], DIR[1], FNAME[0])
        test.assertFalse(op.isdir(DIR[0]))
        test.assertFalse(op.isdir(op.join(DIR[0], DIR[1])))
        test.assertFalse(op.isfile(op.join(DIR[0], DIR[1], FNAME[0])))
        test.assertFalse(f.exists())
        test.assertTrue(f.writeline("hello"))
        test.assertTrue(f.exists())
        test.assertTrue(op.isdir(DIR[0]))
        test.assertTrue(op.isdir(op.join(DIR[0], DIR[1])))
        test.assertTrue(op.isfile(op.join(DIR[0], DIR[1], FNAME[0])))

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()
