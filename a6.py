#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import json
import re
auth = tweepy.OAuthHandler("SuFrrLnvTW1ocbqcwT01fnYFE", "niVFikAwlDqVtwiOrMmEIMlZKD1bSGz6wm2nRJeDbTYmOQfNqZ")
auth.set_access_token("1329423443062886400-bbPsX5k4YDSiJc1KIHSL4NrjG5iVQc", \
	"6jO1VY0F5D8xo7BjDTGyGhrFBY2OVKOr8hBnwVnS7U3AP")

api = tweepy.API(auth)

def WordsCount(tweets):
	l = []
	for t in tweets:
		text = t._json["text"]
		text = re.sub(r'https\S+', '', text, flags=re.MULTILINE)
		text = text.split()
		for w in text:
			l.append((w, len(w)))

	return l

user1 = input("User1:\n")

try:
	tweets1 = api.user_timeline(id=user1,count=10)
except Exception as ex:
	print("Problem found!")
	print(ex)

l = WordsCount(tweets1)
l = list(set(l))
l.sort(key=lambda l: l[1])
min = [l[0] for l in l[:5] ]
print ("Top 5 Μικρότερες:")
print ("\n".join(min))

print ("Top 5 Μεγαλύτερες:")
l.sort(key=lambda l: l[1], reverse = True)
max = [l[0] for l in l[:5] ]
print ("\n".join(max))
