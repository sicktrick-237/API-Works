# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 05:30:28 2019

@author: Omkar Kadam
"""
from apiclient.discovery import build



ytapikey = 'AIzaSyCL9hzV1aexKfLvGF5Vjr73hXfQIOuU5IU'

youtube = build('youtube','v3',developerKey = ytapikey)
# print(type(youtube))


# Basic Syntax

req = youtube.search().list(q='PewDiePie',part='snippet',type='channel',maxResults=10)
res = req.execute()

for each in res['items']:
    print(each['snippet']['title'])