# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 05:30:28 2019

@author: Omkar Kadam
"""
from apiclient.discovery import build



ytapikey = *INSERT API KEY*

youtube = build('youtube','v3',developerKey = ytapikey)
# print(type(youtube))


# Basic Syntax

req = youtube.search().list(q='PewDiePie',part='snippet',type='channel',maxResults=10)
res = req.execute()

for each in res['items']:
    print(each['snippet']['title'])
