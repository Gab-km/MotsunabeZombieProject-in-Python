# -*- coding: utf-8 -*-
import re

def categorize(tweet):
    body = tweet.split('\t')[1]
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
