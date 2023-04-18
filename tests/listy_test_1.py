##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
from testlib import *

from auxly.listy import chunk, smooth, isiterable, iterate

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):
    def test_chunk_1(test):
        data = [1,2,3,4,5,6]
        test.assertEqual([[1,2],[3,4],[5,6]], list(chunk(data, 2)))
        test.assertEqual([[1,2,3],[4,5,6]], list(chunk(data, 3)))
        test.assertEqual([[1,2,3,4],[5,6]], list(chunk(data, 4)))
        test.assertEqual([[1,2,3,4,5],[6]], list(chunk(data, 5)))

    def test_smooth_1(test):
        test.assertEqual([1,2,3,4,5,6], list(smooth([[1,2],[3,4],[5,6]])))
        test.assertEqual([1,2,3,4,5,6], list(smooth([[1,[2]],[[3,4]],[[5],6]])))
        test.assertEqual([1,2,3,4,5,6], list(smooth([[1,[2,[3,[4,[5,[6]]]]]]])))

    def test_isiterable_1(test):
        test.assertTrue(isiterable("abc"))
        test.assertTrue(isiterable([1,2,3]))
        test.assertTrue(isiterable((1,2,3)))
        test.assertFalse(isiterable(123))

    def test_iterate_1(test):
        test.assertEqual(["abc"], list(iterate("abc")))
        test.assertEqual([1,2,3], list(iterate([1,2,3])))

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()
