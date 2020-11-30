# -*- coding: cp1252 -*-
#import pymongo as mg
from twython import Twython, TwythonStreamer
import time
import json
import sys
        
class MyStreamer(TwythonStreamer):
    def __init__(self,APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET):
        TwythonStreamer.__init__(self,APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        #self.tweets = mg.MongoClient().eleicoes.twitter
        #self.users = mg.MongoClient().eleicoes.users
        #self.users.ensure_index('id_str',unique=True)
        self.f = open('FakeNews.json', 'a+')

        
    def on_success(self, data):
        if 'text' in data:
            try:
                #self.tweets.insert(data)
                #self.users.update({"id_str":data['user']['id_str']},{"id_str":data['user']['id_str']},upsert=True )
                json.dump(data,self.f)
                self.f.write('\n')
            except KeyboardInterrupt:
                self.disconnect()

    def on_error(self, status_code, data):
        print (status_code)
        time.sleep(1200)

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

APP_KEY = '-----------------------------------'
APP_SECRET = '--------------------------------------------'

twitter = Twython(APP_KEY, APP_SECRET)

auth = twitter.get_authentication_tokens()
OAUTH_TOKEN = '-------------------------------------------------' #auth['oauth_token']
OAUTH_TOKEN_SECRET = '---------------------------------------------' #auth['oauth_token_secret']


#assuntos = ['shopping','venezuela','esquerdalha']
#query =  ','.join(assuntos)

query =['coronavac']

stream = MyStreamer(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

while True:
    try:
        stream.statuses.filter(track=query, tweet_mode='extended',language='pt')
    except:
        e = sys.exc_info()[0]
        print ('ERROR:', e)
        continue

