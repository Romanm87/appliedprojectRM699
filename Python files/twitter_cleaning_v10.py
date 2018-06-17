# -*- coding: utf-8 -*-
"""
Created on Sun May  6 17:02:01 2018

@author: Roman
"""

# Clean retrieved Twitter data

import csv
import os
import datetime
import html.parser
import string
import re
from nltk.corpus import stopwords
import pandas as pd

html_parser = html.parser.HTMLParser()
os.chdir('c:\\Users\Roman\Documents\HU\ANLY 699-90 Applied Project\Project')

def preprocess(raw_text):    
    text = re.sub(r"http\S+", "", raw_text) # remove links
    text = re.sub("(@[A-Za-z]+)|([^A-Za-z \t])|(\w+:\/\/\S+)", " ", text)  # clean up, remove numbers
    text = re.sub(r" n ", "", text) 
    text = re.sub(r"x\S+", "", text) # removes words starting with "x"    
    words = [i.strip(string.punctuation) for i in text.split() if not len(i) < 3] # remove words with <=2 letters
    text = " ".join(words)        
    words = text.lower().split() # lower case
    stopword_set = set(stopwords.words("english")) # remove stopwords
    meaningful_words = [w for w in words if w not in stopword_set]
    cleaned_word_list = " ".join(meaningful_words)
    return cleaned_word_list

def process_data(dataset, filename):
    tweets_df = pd.read_csv(dataset,header=None)
    num_tweets = tweets_df.shape[0]
    print("Total tweets: " + str(num_tweets))
    cleaned_tweets = []
    print("Beginning processing of tweets at: " + str(datetime.datetime.now()))
    csvFile = open(filename, 'a')
    csvWriter = csv.writer(csvFile, lineterminator = '\n')
    for i in range(num_tweets):
        cleaned_tweet = preprocess(tweets_df.iloc[i][1])
        csvWriter.writerow([tweets_df.iloc[i][0], cleaned_tweet]) # tweet.text.encode('utf-8')])
        cleaned_tweets.append(cleaned_tweet)
    csvFile.close()
    return cleaned_tweets

#cardano
process_data("cardano_04-25(1).csv", 'cardano_04-25(1)_cln.csv')
process_data("cardano_04-26(1).csv", 'cardano_04-26(1)_cln.csv')
process_data("cardano_04-27(1).csv", 'cardano_04-27(1)_cln.csv')
process_data("cardano_04-28(1).csv", 'cardano_04-28(1)_cln.csv')
process_data("cardano_04-29(1).csv", 'cardano_04-29(1)_cln.csv')
process_data("cardano_04-30(1).csv", 'cardano_04-30(1)_cln.csv')
process_data("cardano_05-01(1).csv", 'cardano_05-01(1)_cln.csv')
process_data("cardano_05-02(1).csv", 'cardano_05-02(1)_cln.csv')
process_data("cardano_05-03(1).csv", 'cardano_05-03(1)_cln.csv')
process_data("cardano_05-04(1).csv", 'cardano_05-04(1)_cln.csv')
process_data("cardano_05-05(1).csv", 'cardano_05-05(1)_cln.csv')
process_data("cardano_05-06(1).csv", 'cardano_05-06(1)_cln.csv')
process_data("cardano_05-07(1).csv", 'cardano_05-07(1)_cln.csv')
process_data("cardano_05-08(1).csv", 'cardano_05-08(1)_cln.csv')

#eos
process_data("eos_04-25(1).csv", 'eos_04-25(1)_cln.csv')
process_data("eos_04-26(1).csv", 'eos_04-26(1)_cln.csv')
process_data("eos_04-27(1).csv", 'eos_04-27(1)_cln.csv')
process_data("eos_04-28(1).csv", 'eos_04-28(1)_cln.csv')
process_data("eos_04-29(1).csv", 'eos_04-29(1)_cln.csv')
process_data("eos_04-30(1).csv", 'eos_04-30(1)_cln.csv')
process_data("eos_05-01(1).csv", 'eos_05-01(1)_cln.csv')
process_data("eos_05-02(1).csv", 'eos_05-02(1)_cln.csv')
process_data("eos_05-03(1).csv", 'eos_05-03(1)_cln.csv')
process_data("eos_05-04(1).csv", 'eos_05-04(1)_cln.csv')
process_data("eos_05-05(1).csv", 'eos_05-05(1)_cln.csv')
process_data("eos_05-06(1).csv", 'eos_05-06(1)_cln.csv')
process_data("eos_05-07(1).csv", 'eos_05-07(1)_cln.csv')
process_data("eos_05-08(1).csv", 'eos_05-08(1)_cln.csv')

#ltc
process_data("ltc_04-25(1).csv", 'ltc_04-25(1)_cln.csv')
process_data("ltc_04-26(1).csv", 'ltc_04-26(1)_cln.csv')
process_data("ltc_04-27(1).csv", 'ltc_04-27(1)_cln.csv')
process_data("ltc_04-28(1).csv", 'ltc_04-28(1)_cln.csv')
process_data("ltc_04-29(1).csv", 'ltc_04-29(1)_cln.csv')
process_data("ltc_04-30(1).csv", 'ltc_04-30(1)_cln.csv')
process_data("ltc_05-01(1).csv", 'ltc_05-01(1)_cln.csv')
process_data("ltc_05-02(1).csv", 'ltc_05-02(1)_cln.csv')
process_data("ltc_05-03(1).csv", 'ltc_05-03(1)_cln.csv')
process_data("ltc_05-04(1).csv", 'ltc_05-04(1)_cln.csv')
process_data("ltc_05-05(1).csv", 'ltc_05-05(1)_cln.csv')
process_data("ltc_05-06(1).csv", 'ltc_05-06(1)_cln.csv')
process_data("ltc_05-07(1).csv", 'ltc_05-07(1)_cln.csv')
process_data("ltc_05-08(1).csv", 'ltc_05-08(1)_cln.csv')

#ripple
process_data("ripple_04-25(1).csv", 'ripple_04-25(1)_cln.csv')
process_data("ripple_04-26(1).csv", 'ripple_04-26(1)_cln.csv')
process_data("ripple_04-27(1).csv", 'ripple_04-27(1)_cln.csv')
process_data("ripple_04-28(1).csv", 'ripple_04-28(1)_cln.csv')
process_data("ripple_04-29(1).csv", 'ripple_04-29(1)_cln.csv')
process_data("ripple_04-30(1).csv", 'ripple_04-30(1)_cln.csv')
process_data("ripple_05-01(1).csv", 'ripple_05-01(1)_cln.csv')
process_data("ripple_05-02(1).csv", 'ripple_05-02(1)_cln.csv')
process_data("ripple_05-03(1).csv", 'ripple_05-03(1)_cln.csv')
process_data("ripple_05-04(1).csv", 'ripple_05-04(1)_cln.csv')
process_data("ripple_05-05(1).csv", 'ripple_05-05(1)_cln.csv')
process_data("ripple_05-06(1).csv", 'ripple_05-06(1)_cln.csv')
process_data("ripple_05-07(1).csv", 'ripple_05-07(1)_cln.csv')
process_data("ripple_05-08(1).csv", 'ripple_05-08(1)_cln.csv')

#stellar
process_data("stellar_04-25(1).csv", 'stellar_04-25(1)_cln.csv')
process_data("stellar_04-26(1).csv", 'stellar_04-26(1)_cln.csv')
process_data("stellar_04-27(1).csv", 'stellar_04-27(1)_cln.csv')
process_data("stellar_04-28(1).csv", 'stellar_04-28(1)_cln.csv')
process_data("stellar_04-29(1).csv", 'stellar_04-29(1)_cln.csv')
process_data("stellar_04-30(1).csv", 'stellar_04-30(1)_cln.csv')
process_data("stellar_05-01(1).csv", 'stellar_05-01(1)_cln.csv')
process_data("stellar_05-02(1).csv", 'stellar_05-02(1)_cln.csv')
process_data("stellar_05-03(1).csv", 'stellar_05-03(1)_cln.csv')
process_data("stellar_05-04(1).csv", 'stellar_05-04(1)_cln.csv')
process_data("stellar_05-05(1).csv", 'stellar_05-05(1)_cln.csv')
process_data("stellar_05-06(1).csv", 'stellar_05-06(1)_cln.csv')
process_data("stellar_05-07(1).csv", 'stellar_05-07(1)_cln.csv')
process_data("stellar_05-08(1).csv", 'stellar_05-08(1)_cln.csv')

#eth
process_data("eth_04-25(1).csv", 'eth_04-25(1)_cln.csv')
process_data("eth_04-25(2).csv", 'eth_04-25(2)_cln.csv')
process_data("eth_04-25(3).csv", 'eth_04-25(3)_cln.csv')
process_data("eth_04-25(4).csv", 'eth_04-25(4)_cln.csv')
process_data("eth_04-25(5).csv", 'eth_04-25(5)_cln.csv')
process_data("eth_04-25(6).csv", 'eth_04-25(6)_cln.csv')
process_data("eth_04-26(1).csv", 'eth_04-26(1)_cln.csv')
process_data("eth_04-26(2).csv", 'eth_04-26(2)_cln.csv')
process_data("eth_04-26(3).csv", 'eth_04-26(3)_cln.csv')
process_data("eth_04-26(4).csv", 'eth_04-26(4)_cln.csv')
process_data("eth_04-26(5).csv", 'eth_04-26(5)_cln.csv')
process_data("eth_04-26(6).csv", 'eth_04-26(6)_cln.csv')
process_data("eth_04-27(1).csv", 'eth_04-27(1)_cln.csv')
process_data("eth_04-27(2).csv", 'eth_04-27(2)_cln.csv')
process_data("eth_04-27(3).csv", 'eth_04-27(3)_cln.csv')
process_data("eth_04-27(4).csv", 'eth_04-27(4)_cln.csv')
process_data("eth_04-27(5).csv", 'eth_04-27(5)_cln.csv')
process_data("eth_04-27(6).csv", 'eth_04-27(6)_cln.csv')
process_data("eth_04-28(1).csv", 'eth_04-28(1)_cln.csv')
process_data("eth_04-28(2).csv", 'eth_04-28(2)_cln.csv')
process_data("eth_04-28(3).csv", 'eth_04-28(3)_cln.csv')
process_data("eth_04-28(4).csv", 'eth_04-28(4)_cln.csv')
process_data("eth_04-28(5).csv", 'eth_04-28(5)_cln.csv')
process_data("eth_04-28(6).csv", 'eth_04-28(6)_cln.csv')
process_data("eth_04-29(1).csv", 'eth_04-29(1)_cln.csv')
process_data("eth_04-29(2).csv", 'eth_04-29(2)_cln.csv')
process_data("eth_04-29(3).csv", 'eth_04-29(3)_cln.csv')
process_data("eth_04-29(4).csv", 'eth_04-29(4)_cln.csv')
process_data("eth_04-29(5).csv", 'eth_04-29(5)_cln.csv')
process_data("eth_04-29(6).csv", 'eth_04-29(6)_cln.csv')
process_data("eth_04-30(1).csv", 'eth_04-30(1)_cln.csv')
process_data("eth_04-30(2).csv", 'eth_04-30(2)_cln.csv')
process_data("eth_04-30(3).csv", 'eth_04-30(3)_cln.csv')
process_data("eth_04-30(4).csv", 'eth_04-30(4)_cln.csv')
process_data("eth_04-30(5).csv", 'eth_04-30(5)_cln.csv')
process_data("eth_04-30(6).csv", 'eth_04-30(6)_cln.csv')
process_data("eth_05-01(1).csv", 'eth_05-01(1)_cln.csv')
process_data("eth_05-01(2).csv", 'eth_05-01(2)_cln.csv')
process_data("eth_05-01(3).csv", 'eth_05-01(3)_cln.csv')
process_data("eth_05-01(4).csv", 'eth_05-01(4)_cln.csv')
process_data("eth_05-01(5).csv", 'eth_05-01(5)_cln.csv')
process_data("eth_05-01(6).csv", 'eth_05-01(6)_cln.csv')
process_data("eth_05-02(1).csv", 'eth_05-02(1)_cln.csv')
process_data("eth_05-02(2).csv", 'eth_05-02(2)_cln.csv')
process_data("eth_05-02(3).csv", 'eth_05-02(3)_cln.csv')
process_data("eth_05-02(4).csv", 'eth_05-02(4)_cln.csv')
process_data("eth_05-02(5).csv", 'eth_05-02(5)_cln.csv')
process_data("eth_05-02(6).csv", 'eth_05-02(6)_cln.csv')
process_data("eth_05-03(1).csv", 'eth_05-03(1)_cln.csv')
process_data("eth_05-03(2).csv", 'eth_05-03(2)_cln.csv')
process_data("eth_05-03(3).csv", 'eth_05-03(3)_cln.csv')
process_data("eth_05-03(4).csv", 'eth_05-03(4)_cln.csv')
process_data("eth_05-03(5).csv", 'eth_05-03(5)_cln.csv')
process_data("eth_05-03(6).csv", 'eth_05-03(6)_cln.csv')
process_data("eth_05-04(1).csv", 'eth_05-04(1)_cln.csv')
process_data("eth_05-04(2).csv", 'eth_05-04(2)_cln.csv')
process_data("eth_05-04(3).csv", 'eth_05-04(3)_cln.csv')
process_data("eth_05-04(4).csv", 'eth_05-04(4)_cln.csv')
process_data("eth_05-04(5).csv", 'eth_05-04(5)_cln.csv')
process_data("eth_05-04(6).csv", 'eth_05-04(6)_cln.csv')
process_data("eth_05-05(1).csv", 'eth_05-05(1)_cln.csv')
process_data("eth_05-05(2).csv", 'eth_05-05(2)_cln.csv')
process_data("eth_05-05(3).csv", 'eth_05-05(3)_cln.csv')
process_data("eth_05-05(4).csv", 'eth_05-05(4)_cln.csv')
process_data("eth_05-05(5).csv", 'eth_05-05(5)_cln.csv')
process_data("eth_05-05(6).csv", 'eth_05-05(6)_cln.csv')
process_data("eth_05-06(1).csv", 'eth_05-06(1)_cln.csv')
process_data("eth_05-06(2).csv", 'eth_05-06(2)_cln.csv')
process_data("eth_05-06(3).csv", 'eth_05-06(3)_cln.csv')
process_data("eth_05-06(4).csv", 'eth_05-06(4)_cln.csv')
process_data("eth_05-06(5).csv", 'eth_05-06(5)_cln.csv')
process_data("eth_05-06(6).csv", 'eth_05-06(6)_cln.csv')
process_data("eth_05-07(1).csv", 'eth_05-07(1)_cln.csv')
process_data("eth_05-07(2).csv", 'eth_05-07(2)_cln.csv')
process_data("eth_05-07(3).csv", 'eth_05-07(3)_cln.csv')
process_data("eth_05-07(4).csv", 'eth_05-07(4)_cln.csv')
process_data("eth_05-07(5).csv", 'eth_05-07(5)_cln.csv')
process_data("eth_05-07(6).csv", 'eth_05-07(6)_cln.csv')
process_data("eth_05-08(1).csv", 'eth_05-08(1)_cln.csv')
process_data("eth_05-08(2).csv", 'eth_05-08(2)_cln.csv')
process_data("eth_05-08(3).csv", 'eth_05-08(3)_cln.csv')
process_data("eth_05-08(4).csv", 'eth_05-08(4)_cln.csv')
process_data("eth_05-08(5).csv", 'eth_05-08(5)_cln.csv')
process_data("eth_05-08(6).csv", 'eth_05-08(6)_cln.csv')


