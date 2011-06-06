# -*- coding: utf-8 -*-
import re

def categorize(tweet):
    body = tweet.split('\t')[1]
    if re.search("#\w", body):
        return "!Hashtag\t" + body
    if re.search("^@\w", body):
        return "Reply\t" + body
    return "Normal\t" + body
