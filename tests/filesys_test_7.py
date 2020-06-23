# -*- coding: utf-8 -*-
##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from testlib import *

from auxly.filesys import File

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

UTF8_STR = u"ÁÍÓÚÀÈÌÒÙAEIOU"

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):
    def test_file_1(test):
        """Basic File usage."""
        p = FNAME[0]
        f = File(p)
        test.assertFalse(f.exists())
        test.assertTrue(f.write(UTF8_STR))
        test.assertTrue(f.exists())
        test.assertEqual(UTF8_STR, f.read())
        test.assertEqual(None, f.read(encoding="ascii"))
        test.assertEqual(FNAME[0], f.name)
        test.assertTrue(op.isabs(f.path))

    def test_file_2(test):
        """Basic File usage."""
        p = FNAME[0]
        f = File(p)
        test.assertFalse(f.exists())
        test.assertFalse(f.write(UTF8_STR, encoding="ascii"))
        test.assertEqual(FNAME[0], f.name)
        test.assertTrue(op.isabs(f.path))

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()
