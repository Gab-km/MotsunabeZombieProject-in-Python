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
        result = mzp.categorize(self.posted_time + "gab_km\tほげ #fuga")
        self.assertEqual("!Hashtag\tほげ #fuga", result)

    def test_リプライTweetをReply_tab_tweetbodyとして返す(self):
        result = mzp.categorize(self.posted_time + "gab_km\t@Alice はげ")
        self.assertEqual("Reply\t@Alice はげ", result)

    def test_メンションTweetをMention_tab_tweetbodyとして返す(self):
        result = mzp.categorize(self.posted_time + "gab_km\tふげ @Alice ひげ")
        self.assertEqual("Mention\tふげ @Alice ひげ", result)

    def test_ドット付きリプライTweetもメンションとして扱う(self):
        result = mzp.categorize(self.posted_time + "gab_km\t.@Alice へげ")
        self.assertEqual("Mention\t.@Alice へげ", result)

    def test_ハッシュタグとリプライTweetでHashtag_Replyの順で返す(self):
        result = mzp.categorize(self.posted_time + "gab_km\t@Alice ほげ #bar")
        self.assertEqual("!Hashtag,Reply\t@Alice ほげ #bar", result)

    def test_リプライとメンションTweetでReply_Mentionの順で返す(self):
        result = mzp.categorize(self.posted_time + "gab_km\t@Alice @Bob はげ")
        self.assertEqual("Reply,Mention\t@Alice @Bob はげ", result)

    def test_ハッシュタグとメンションTweetでHashtag_Mentionの順で返す(self):
        result = mzp.categorize(self.posted_time + "gab_km\tふげ @Alice #blur")
        self.assertEqual("!Hashtag,Mention\tふげ @Alice #blur", result)

    def test_Web上からツイートを取得して振り分けられる(self):
        url = "http://tddbc.heroku.com/mzp/public_timeline"
        result = mzp.categorize_web_tweet(url)
        self.assertListEqual(self.expected, result)

    expected = ["Normal\t試しにつぶやいてみるわ",
                "Reply\t@Bob これがreplyね",
                "Mention\tmentionは@Bobでいいのかしら？",
                "Reply\t@Alice 頑張っているみたいだね。",
                "Normal\t僕もぼちぼち作業しようかな。",
                "Normal\tReTweetって2種類あるのね、知らなかったわ…",
                "!Hashtag\t僕は#hashtagを試しておこう。",
                "Reply,Mention\t@Charlie @Alice " + \
                    "明日の13時から詳細を詰めたいんだけど、空いてるかな？",
                "Normal\tとりあえずはこんな感じかしら。",
                "Reply\t@Bob 私は空いてるわ",
                "Normal\t3時のおやつタイムだ！",
                "Normal\tおっと、Aliceから返事がきてる。" + \
                    "…ふむふむ、となるとCharlie待ちかな。",
                "Reply,Mention\t@Bob 空いてるよ。" + \
                    "部屋は君か@Aliceが押さえておいてくれると助かるかな。",
                "Reply,Mention\t@Charlie @Alice " + \
                    "部屋はすでに押さえているよ。" + \
                    "メールを送ったから場所の確認よろしく！",
                "Normal\t夜更かしは肌に悪いから寝るわ",
                "Mention\tふむ RT @Alice: ReTweetって2種類あるのね",
                "Normal\tよーし、短縮URLについて調べるぞー",
                "!Hashtag\t本日つぶやいたユーザの記録 2011-04-01 #kiroku",
                "Mention\tMT @Alice: これも非公式RTね",
                "!Hashtag,Mention\t2011-04-01 @Aliceのつぶやき 7件 #kiroku"
                ]

if __name__ == '__main__':
    suite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(MzpTest)
        ])
    with open('testlog.xml', 'w') as f:
        runner = xmlrunner.XMLTestRunner(f)
        runner.run(suite)
    unittest.main()
