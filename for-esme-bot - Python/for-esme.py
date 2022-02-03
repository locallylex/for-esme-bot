#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
print('tweepy imported')
 
#Twitter application information:
consumerKey = #redacted
consumerSecret = #redacted
accessKey = #redacted
accessSecret = #redacted
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)
api = tweepy.API(auth)

print('in loving memory of jd')

#keep track of which line we are at
currentLinetxt=open("currentLine.txt","r")
currentLine=currentLinetxt.readlines()
currentLinetxt.close()
print(currentLine)


with open('esme.txt') as fp:
    for line in fp:
        api.update_status(status=line)
        print(line)
        
        

        #update currentLine.txt file
        currentLinetxt=open("currentLine.txt","w")
        currentLinetxt.truncate()
        currentLinetxt.write(str(line))
        currentLinetxt.close()
        
        time.sleep(60*60*2) #Tweet every 2 hours
        #time.sleep(900)#Tweet every 15 minutes

        
