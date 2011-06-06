# -*- coding: utf-8 -*-
import re

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
