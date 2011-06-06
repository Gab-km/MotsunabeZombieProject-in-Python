# -*- coding: utf-8 -*-
import sys
import unittest
import xmlrunner
import mzp_main as mzp

class MzpTest(unittest.TestCase):
    def test_gab_km_tab_あいうえおをNormal_tab_あいうえおとして返す(self):
        result = mzp.categorize("gab_km\tあいうえお")
        self.assertEqual("Normal\tあいうえお", result)

    def test_Alice_tab_かきくきこをNormal_tab_かきくけことして返す(self):
        result = mzp.categorize("Alice\tかきくけこ")
        self.assertEqual("Normal\tかきくけこ", result)

    def test_ハッシュタグ付きのTweetをハッシュタグ付きとして扱う(self):
        result = mzp.categorize("gab_km\tほげ #fuga")
        self.assertEqual("!Hashtag\tほげ #fuga", result)

    def test_リプライTweetをReply_tab_tweetbodyとして返す(self):
        result = mzp.categorize("gab_km\t@Alice はげ")
        self.assertEqual("Reply\t@Alice はげ", result)

if __name__ == '__main__':
    suite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(MzpTest)
        ])
    with open('testlog.xml', 'w') as f:
        runner = xmlrunner.XMLTestRunner(f)
        runner.run(suite)
    unittest.main()
