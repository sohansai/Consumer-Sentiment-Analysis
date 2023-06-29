#source: https://github.com/MuthuveerapandiyanM/twitter-scraper---python-streamlit/blob/main/streamApp.py

import streamlit as st

import snscrape.modules.twitter as sntwitter

import datetime

import json

import pandas as pd

from pymongo import MongoClient


#Import Required Packages
import snscrape.modules.twitter as sntwitter
import streamlit as st
import pandas as pd
import pymongo
import time
from datetime import date
import json

# Connected to  DATABASE
client = pymongo.MongoClient("mongodb+srv://Muthu:Rajesh23@cluster0.tib5p2o.mongodb.net/?retryWrites=true&w=majority")
twtdb = client.StreamApp
twtdb_main = twtdb.twitterdata

tweets_df = pd.DataFrame()
dfm = pd.DataFrame()

#Streamlit Customize
st.title("Twitter Scraping")
st.write('''This is a web app created using Streamlit.We have name for that app which is Twitter Scraper App.  
             It scrapes the twitter data for the given hashtag/ keyword for the given period.
             The tweets which can be dowloaded as CSV or a JSON file.''')
option = st.selectbox('How would you like the data to be searched?',('Keyword', 'Hashtag'))
word = st.text_input('Please enter a '+option)
start = st.date_input("Select the start date")
end = st.date_input("Select the end date")
tweet_c = st.slider('How many tweets to scrape', 0, 1000, 5, 10)
tweets_list = []

# SCRAPE DATA USING TwitterSearchScraper and TwitterHashtagScraper
if word:
    if option=='Keyword':
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{word} + since:{start} until:{end}').get_items()):
            if i>tweet_c:
                break
            tweets_list.append([ tweet.id, tweet.date,  tweet.content, tweet.lang, tweet.user.username, tweet.replyCount, tweet.retweetCount,tweet.likeCount, tweet.source, tweet.url ])
        tweets_df = pd.DataFrame(tweets_list, columns=['ID','Date','Content', 'Language', 'Username', 'ReplyCount', 'RetweetCount', 'LikeCount','Source', 'Url'])
    else:
        for i,tweet in enumerate(sntwitter.TwitterHashtagScraper(f'{word} + since:{start} until:{end}').get_items()):
            if i>tweet_c:
                break
            tweets_list.append([ tweet.id, tweet.date,  tweet.content, tweet.lang, tweet.user.username, tweet.replyCount, tweet.retweetCount,tweet.likeCount, tweet.source, tweet.url ])
        tweets_df = pd.DataFrame(tweets_list, columns=['ID','Date','Content', 'Language', 'Username', 'ReplyCount', 'RetweetCount', 'LikeCount','Source', 'Url'])
else:
  st.success('Lets go', icon="✅")

@st.cache_data # IMPORTANT: Cache the conversion to prevent computation on every rerun
def convert_df(df):
    return tweets_df.to_csv().encode('utf-8')

if not tweets_df.empty:
    csv = convert_df(tweets_df)
# SHOW TWEETS
    if st.button('Show Tweets'):
        st.write(tweets_df)
    st.download_button(label="Download data as CSV",data=csv,file_name='Twitter_data.csv',mime='text/csv',)

# DOWNLOAD AS JSON
    json_string = tweets_df.to_json(orient ='records')
    st.download_button(label="Download data as JSON",file_name="Twitter_data.json",mime="application/json",data=json_string,)

# UPLOAD DATA TO DATABASE
    if st.button('Upload Tweets to Database'):
        coll=word
        coll=coll.replace(' ','_')+'_Tweets'
        mycoll=twtdb[coll]
        dict=tweets_df.to_dict('records')
        if dict:
            mycoll.insert_many(dict)
            ts = time.time()
            mycoll.update_many({}, {"$set": {"KeyWord_or_Hashtag": word+str(ts)}}, upsert=False, array_filters=None)
            st.success('Successfully uploaded to database', icon="✅")
            st.balloons()
        else:
            st.warning('Cant upload because there are no tweets', icon="⚠️")



# DISPLAY THE DOCUMENTS IN THE SELECTED COLLECTION
if not dfm.empty:
    st.write( len(dfm),'Records Found')
    st.write(dfm)




