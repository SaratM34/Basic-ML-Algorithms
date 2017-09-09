from textblob import TextBlob
import tweepy
import csv

consumer_key = 'M6wMSsltNv1aUuKpe7ou2oBvs'
consumer_secret = 'AmVNUgspDUZLDlidooS207HW9AZxk1Coy5hmV1UIhfjGXyaTHv'

access_token = 	'327473973-OqIeRpAawJvQEfXYqWAW8GvrBjc7IiSo6i2lVlLe'
access_token_secret = 'WbMpEsn19gV1K7qPlz4wiGv1sEcfzR5OABDHZDLZ59HBY'


#To Authenticate with twitter

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)



api = tweepy.API(auth) # access to twitter API

# with API variable we can create tweets, delete tweets, find twitter users, search for topics

public_tweets = api.search('Trump') # searches tweets with keyword 'Trump'

with open('names.csv', 'w') as csvfile:
	fieldnames = ['Tweet_text', 'Sentiment']
	writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
	writer.writeheader()
	
	for tweet in public_tweets:
		analysis = TextBlob(tweet.text)
		if(analysis.sentiment.polarity > 0):
			writer.writerow({'Tweet_text': tweet.text.encode('utf-8'), 'Sentiment': 'Positive'})
		else:
			writer.writerow({'Tweet_text': tweet.text.encode('utf-8'), 'Sentiment': 'Negative'})

