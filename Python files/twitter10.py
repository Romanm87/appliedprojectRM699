# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

# disable avast first!   
# environment: crypto

import tweepy
import csv
import os
import time
from time import sleep

#os.getcwd()
os.chdir('c:\\Users\Roman\Documents\HU\ANLY 699-90 Applied Project\Project')

consumer_key = 'xxxxxxxxxx'
consumer_secret = 'xxxxxxxxxx'
access_token = 'xxxxxxxxxx'
access_token_secret = 'xxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Example (150 calls within 15 min)
#csvFile = open('gold3.csv', 'a')
#csvWriter = csv.writer(csvFile)
#for tweet in tweepy.Cursor(api.search,q="#gold",count=#tweets per page,
#                           lang="en",
#                           since="2018-04-20").items(#pages):
#    print (tweet.created_at, tweet.text)
#    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

###original from: https://gist.github.com/vickyqian/f70e9ab3910c7c290d9d715491cde44c
# Open/Create a file to append data


#5/4 00:00: 992192090309357570
#5/4 04:00: 992252485669502977
#5/4 08:00: 992312885983330305
#5/4 12:00: 992373533375426560
csvFile = open('eth_05-04(1).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 992192090309357570,
                           max_id = 992252485669502977).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)

############CONT HERE

#5/6 00:00: 992916864870309889
#5/7 00:00: 993279250852712449
csvFile = open('cardano_05-06(1).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#cardano",count=250,
                           lang="en",
                           since_id = 992916864870309889,
                           max_id =  993279250852712449).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
csvFile = open('stellar_05-06(1).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#stellar",count=250,
                           lang="en",
                           since_id = 992916864870309889,
                           max_id =  993279250852712449).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
csvFile = open('ripple_05-06(1).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ripple",count=250,
                           lang="en",
                           since_id = 992916864870309889,
                           max_id =  993279250852712449).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
csvFile = open('ltc_05-06(1).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#litecoin",count=250,
                           lang="en",
                           since_id = 992916864870309889,
                           max_id =  993279250852712449).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
csvFile = open('eos_05-06(1).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#eos",count=250,
                           lang="en",
                           since_id = 992916864870309889,
                           max_id =  993279250852712449).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)



#5/6 00:00: 992916864870309889
#5/6 04:00: 992977262529187841
#5/6 08:00: 993037658480881664
#5/6 12:00: 993098059017064449
#5/6 16:00: 993158454717091840
#5/6 20:00: 993218852841455623
#5/7 00:00: 993279250852712449
csvFile = open('eth_05-06(1).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 992916864870309889,
                           max_id = 992977262529187841).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
csvFile = open('eth_05-06(2).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 992977262529187841,
                           max_id = 993037658480881664).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
csvFile = open('eth_05-06(3).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 993037658480881664,
                           max_id = 993098059017064449).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
#5/6 12:00: 993098059017064449
#5/6 16:00: 993158454717091840
#5/6 20:00: 993218852841455623
#5/7 00:00: 993279250852712449
csvFile = open('eth_05-06(4).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 993098059017064449,
                           max_id = 993158454717091840).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
################ CONTINUE HERE ###################
time.sleep(930)
csvFile = open('eth_05-06(5).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 993158454717091840,
                           max_id = 993218852841455623).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)

csvFile = open('eth_05-06(6).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 993218852841455623,
                           max_id = 993279250852712449).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
#5/7 00:00: 993279250852712449
#5/7 04:00: 993339649320943616
#5/7 08:00: 993400048472948736
#5/7 12:00: 993460447251755008
#5/7 16:00: 993520842993754114
#5/7 20:00: 993581242653331456
#5/8 00:00: 993641640077287426
csvFile = open('eth_05-07(1).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 993279250852712449,
                           max_id = 993339649320943616).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
csvFile = open('eth_05-07(2).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 993339649320943616,
                           max_id = 993400048472948736).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
csvFile = open('eth_05-07(3).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 993400048472948736,
                           max_id = 993460447251755008).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
#5/7 12:00: 993460447251755008
#5/7 16:00: 993520842993754114
#5/7 20:00: 993581242653331456
#5/8 00:00: 993641640077287426
csvFile = open('eth_05-07(4).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 993460447251755008,
                           max_id = 993520842993754114).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
csvFile = open('eth_05-07(5).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 993520842993754114,
                           max_id = 993581242653331456).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
csvFile = open('eth_05-07(6).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 993581242653331456,
                           max_id = 993641640077287426).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
#5/7 00:00: 993279250852712449
#5/8 00:00: 993641640077287426
csvFile = open('cardano_05-07(1).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#cardano",count=250,
                           lang="en",
                           since_id = 993279250852712449,
                           max_id =  993641640077287426).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
csvFile = open('stellar_05-07(1).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#stellar",count=250,
                           lang="en",
                           since_id = 993279250852712449,
                           max_id =  993641640077287426).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
csvFile = open('ripple_05-07(1).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ripple",count=250,
                           lang="en",
                           since_id = 993279250852712449,
                           max_id =  993641640077287426).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
csvFile = open('ltc_05-07(1).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#litecoin",count=250,
                           lang="en",
                           since_id = 993279250852712449,
                           max_id =  993641640077287426).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
csvFile = open('eos_05-07(1).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#eos",count=250,
                           lang="en",
                           since_id = 993279250852712449,
                           max_id =  993641640077287426).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)


#5/8 00:00: 993641640077287426
#5/8 04:00: 993702039132737536
#5/8 08:00: 993762436212764672
#5/8 12:00: 993822836115550208
#5/8 16:00: 993883484761534465
#5/8 20:00: 993943629570936833
#5/9 00:00: 994004025589796864
csvFile = open('eth_05-08(1).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 993641640077287426,
                           max_id = 993702039132737536).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
csvFile = open('eth_05-08(2).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 993702039132737536,
                           max_id = 993762436212764672).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
csvFile = open('eth_05-08(3).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 993762436212764672,
                           max_id = 993822836115550208).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
#5/8 12:00: 993822836115550208
#5/8 16:00: 993883484761534465
#5/8 20:00: 993943629570936833
#5/9 00:00: 994004025589796864
csvFile = open('eth_05-08(4).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 993822836115550208,
                           max_id = 993883484761534465).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
csvFile = open('eth_05-08(5).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 993883484761534465,
                           max_id = 993943629570936833).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
csvFile = open('eth_05-08(6).csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator = '\n')
for tweet in tweepy.Cursor(api.search,q="#ethereum",count=250,
                           lang="en",
                           since_id = 993943629570936833,
                           max_id = 994004025589796864).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
time.sleep(930)
#5/8 00:00: 993641640077287426
#5/9 00:00: 994004025589796864






