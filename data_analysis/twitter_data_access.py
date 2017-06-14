from tweepy import OAuthHandler, Stream, API
import json
from tweepy.streaming import StreamListener

consumer_key = 'vttGSL2Lou3d1LMqnPu2c114r'
consumer_secret = 'V2vIE9ZRLe62aqf3Ka4ds2yie1wyDathrbcjRbxmMPpGWad4f3'
access_token =  '24293029-HDKDTcwMv76otEbtwPtafhzBthwXrf6Dg8d7lWK3x'
access_token_secret = 'PEeh5xVHunUcnf37jxQaWyoAAiBlV8ArAsLbFgddTBh4p'

auth = OAuthHandler(consumer_key,
			consumer_secret)

auth.set_access_token(access_token, access_token_secret)

class PrintListener(StreamListener):
	def on_status(self, status):
		if not status.text[:3] == 'RT ':
			print(status.text)
			print(status.author.screen_name,
				status.created_at,
				status.source,
				'\n')

	def on_error(self, status_code):
		print("Error Code: {}".format(status_code))
		return True # Keep stream alive

	def on_timeout(self):
		print("Listener timed out!")
		return True # Keep stream alive


def print_to_terminal():
	listener = PrintListener()
	stream = Stream(auth, listener)
	languages = ('en',)
	stream.sample(languages=languages)

def pull_down_tweets(screen_name):
	api = API(auth)
	tweets = api.user_timeline(screen_name=screen_name, count=200)
	for tweet in tweets:
		print(json.dumps(tweet._json, indent=4))
	

if __name__ == '__main__':
#	print_to_terminal()
	pull_down_tweets(auth.username)



