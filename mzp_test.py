# -*- coding: utf-8 -*-
import sys
import unittest
import xmlrunner
import mzp_main as mzp

class MzpTest(unittest.TestCase):
    posted_time = "2011/06/07 00:36:10\t"
    def test_普通のTweetを普通として扱う(self):
        result = mzp.categorize(self.posted_time + "gab_km\tあいうえお")
        self.assertEqual("Normal\tあいうえお", result)

    def test_ハッシュタグ付きのTweetをハッシュタグ付きとして扱う(self):
        result = mzp.categorize("gab_km\tほげ #fuga")
        self.assertEqual("!Hashtag\tほげ #fuga", result)

    def test_リプライTweetをReply_tab_tweetbodyとして返す(self):
        result = mzp.categorize("gab_km\t@Alice はげ")
        self.assertEqual("Reply\t@Alice はげ", result)

    def test_メンションTweetをMention_tab_tweetbodyとして返す(self):
        result = mzp.categorize("gab_km\tふげ @Alice ひげ")
        self.assertEqual("Mention\tふげ @Alice ひげ", result)

    def test_ドット付きリプライTweetもメンションとして扱う(self):
        result = mzp.categorize("gab_km\t.@Alice へげ")
        self.assertEqual("Mention\t.@Alice へげ", result)

    def test_ハッシュタグとリプライTweetでHashtag_Replyの順で返す(self):
        result = mzp.categorize("gab_km\t@Alice ほげ #bar")
        self.assertEqual("!Hashtag,Reply\t@Alice ほげ #bar", result)

    def test_リプライとメンションTweetでReply_Mentionの順で返す(self):
        result = mzp.categorize("gab_km\t@Alice @Bob はげ")
        self.assertEqual("Reply,Mention\t@Alice @Bob はげ", result)

    def test_ハッシュタグとメンションTweetでHashtag_Mentionの順で返す(self):
        result = mzp.categorize("gab_km\tふげ @Alice #blur")
        self.assertEqual("!Hashtag,Mention\tふげ @Alice #blur", result)

if __name__ == '__main__':
    suite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(MzpTest)
        ])
    with open('testlog.xml', 'w') as f:
        runner = xmlrunner.XMLTestRunner(f)
        runner.run(suite)
    unittest.main()
