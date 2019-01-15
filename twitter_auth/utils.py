import tweepy

CONSUMER_KEY = 'fdeOJrxMU7xE1KuflEQudxAg8'
CONSUMER_SECRET = 'lGgJXT5sqGPEVPA4cvxZGuJk3HKPARZCsveptj1ihvbXE1YwT4'

def get_api(request):
	# set up and return a twitter api object
	oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	access_key = request.session['access_key_tw']
	access_secret = request.session['access_secret_tw']
	oauth.set_access_token(access_key, access_secret)
	api = tweepy.API(oauth)
	return api
