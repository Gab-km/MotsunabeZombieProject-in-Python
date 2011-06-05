# -*- coding: utf-8 -*-
import re

def categorize(tweet):
    if re.search("#\w", tweet):
        return "!Hashtag\t" + tweet.split('\t')[1]
    return "Normal\t" + tweet.split('\t')[1]
