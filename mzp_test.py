# -*- coding: utf-8 -*-
import sys
import unittest
import xmlrunner
import mzp_main as mzp

class MzpTest(unittest.TestCase):
    def test_gab_km_tab_あいうえおをNormal_tab_あいうえおとして返す(self):
        result = mzp.categorize("gab_km\tあいうえお")
        self.assertEqual("Normal\tあいうえお", result)

if __name__ == '__main__':
    suite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(MzpTest)
        ])
    with open('testlog.xml', 'w') as f:
        runner = xmlrunner.XMLTestRunner(f)
        runner.run(suite)
    unittest.main()
