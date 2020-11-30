import tweepy
from tweepy import OAuthHandler
from tweepy import API,TweepError,Cursor
import csv
from collections import ChainMap

APP_KEY = '-----------------------------------'
APP_SECRET = '-----------------------------------'
OAUTH_TOKEN = '-----------------------------------' #auth['oauth_token']
OAUTH_TOKEN_SECRET = '-----------------------------------' #auth['oauth_token_secret']

auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth
                ,wait_on_rate_limit=True, wait_on_rate_limit_notify=True
)

# Open/create a file to append data to
csvFile = open('tudo.csv', 'a',newline='')
csvFile2 = open('filtrado.csv','a',newline='')

#Use csv writer
fields=["User","Location","Tweeter","Mentions"]
fields2=["User","Mentions"]
csvWriter = csv.DictWriter(csvFile,fieldnames=fields)
csvWriter2 = csv.DictWriter(csvFile2,fieldnames=fields2)
csvWriter.writeheader()

keywords = "laranjal boulos -fake"
date = '2020-11-01'
until = '2020-11-28'


for tweet in tweepy.Cursor(api.search,
                           q = keywords,
                           since = date,
                           until = until,
                           #lang = "pt",
                           tweet_mode='extended').items(300000):

    # Write a row to the CSV file. I use encode UTF-8
    #csvWriter.writerow([tweet.created_at,tweet.user.screen_name,tweet.user.location, tweet.full_text.encode('utf-8')])
    entities = tweet.entities.get('user_mentions')
    entities = dict(ChainMap(*entities))

    person_dict = {'User': tweet.user.screen_name,
    #'Location': tweet.user.location,
    'Tweeter' : tweet.full_text.encode('ascii',errors='ignore'),
    'Mentions': entities.get('screen_name')
    }
    person_dict2 = {
    'Mentions': entities.get('screen_name'),
    'User': tweet.user.screen_name
    }
    
    csvWriter.writerow(person_dict)
    csvWriter2.writerow(person_dict2)


csvFile.close()
input('Press ENTER to exit')