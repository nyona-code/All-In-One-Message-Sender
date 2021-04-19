import tweepy
from flask import jsonify #handles the json dict inside the tweepy verify credientials

def sendTweet(tweetMessage):
	api = auth()

	# .update_status allows us to post tweets
	api.update_status(tweetMessage)

def sendTweetImage(tweetMessage, Image):
	api = auth()

	media = api.media_upload(Image)

	api.update_status(tweetMessage, media_ids=[media.media_id])



def sendDM():
	api = auth()
	message = input("DM: ")
	user = input("user: ")

	user = api.get_user("WaleedAbdul0") #replace user

	recipient_id = user.id_str 


	dM = api.send_direct_message(recipient_id, message)


def auth():
	#API_KEY
	consumer_key = "n9KnlQf3vxERxHT2HOIb1UKlU"
	#API_SECRET_KEY
	consumer_secret = "lTZhX91YN2goYiHmdgj4Ol5LSF5bh0fKB2V991F0DQFei8UWGG"

	BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAGGWMQEAAAAAATAZNVKGdsZmfI94%2B5kblF1XTc0%3DrdFrI5RbIhl70yoUNrshHPcw4DjFaFxksSZfXkM7lu0AlxkRZY" 

	access_token = "1357087883996368898-WakEtk5CFVO7rkzYOQ9V0QdchrYuho"
	access_token_secret = "bfMiShHCx44TSfabSj3HRkwUyN9DDHabGlCIzTvmNIPuC"

	#This sets up the tweepy package using the codes that were given us by the twitter for developers website
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	#once the codes have been set up send it to the twitter api to access the project and the account
	api = tweepy.API(auth)

	#Verifies that it connected to an account then prints the name of said account

	if(api.verify_credentials() != False):
		print("Accessed account:", api.me().screen_name)
	else:
		print("User verification failed.")

	return api
