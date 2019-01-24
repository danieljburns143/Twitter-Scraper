#!/usr/bin/env python3

import tweepy

class RESTfulClient():

	def __init__(self):
		self.consumerKey = '6n8Rxt4Sr8ARar0BPbY0DDWPn'
		self.consumerSecret = 'mKldvjoCpOmSx4Y8Clfg6nuVHI6yzNMXOPcVURpYmeUFbU4mm5'
		self.accessToken = '4493310441-9zLVskrEABGDohyU1DcdKfOzhAmtCkcmtNHKTS3'
		self.accessSecret = 'MUYvMQAEHENqbA7qG2UdfB6v3BUZp212UJXqprpuGwhjM'
		self.initializeAPI(self.consumerKey, self.consumerSecret, self.accessToken, \
			self.accessSecret)
	
	def initializeAPI(self, consumerKey, consumerSecret, accessToken, accessSecret):
		self.auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
		self.auth.set_access_token(accessToken, accessSecret)
		self.api = tweepy.API(self.auth)
	
	def getAvailableTrendLocations(self):
		return self.api.trends_available()
	
	def getTopTrends(self, woeid):
		return self.api.trends_place(woeid)
