from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__ = "5624dc41-775a-4d17-ac42-14a0d5c41d1a"

__docformat__ = "restructuredtext en"

import unittest

from pythonids.pythondist import PYE_SYNTAXTYPE, PYE_SYNTAXTYPE_MAJOR, PYE_SYNTAXTYPE_MINOR


class CallUnits(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None

    def testCase010(self):
        self.assertEqual(PYE_SYNTAXTYPE, 0x7f800000)

    def testCase020(self):
        self.assertEqual(PYE_SYNTAXTYPE_MAJOR, 0x70000000)

    def testCase030(self):
        self.assertEqual(PYE_SYNTAXTYPE_MINOR, 0x0f800000)



if __name__ == '__main__':
    unittest.main()
