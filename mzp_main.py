# -*- coding: utf-8 -*-
import re
import urllib.request

def categorize(tweet):
    [posted_time, screen_name, body] = tweet.split('\t')
    category = []
    if re.search("#\w", body):
        category.append("!Hashtag")
    if re.search("^@\w", body):
        category.append("Reply")
    if re.search(".@\w", body):
        category.append("Mention")
    if len(category) > 0:
        return ','.join(category) + "\t" + body
    return "Normal\t" + body

def categorize_web_tweet(url):
    with urllib.request.urlopen(url) as f:
        raw_tweets = f.read().decode('utf_8_sig')
        return list(map(categorize,
                        filter(lambda x: x != '', raw_tweets.split('\n'))))
