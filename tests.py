#!/usr/env/python3
# Naz-Al Islam

# UNITTEST

import unittest

from dcb_copy import *

a = CircularBuffer([1,2,3])

class CircularBufferTest(unittest.TestCase):
    def testLengthOfBuffer(self):
        self.assertEqual(len(a), 3)
    def testGetItem(self):
        self.assertEqual(a.__getitem__(1), 2)







unittest.main()
