from rest_framework import generics
from django.http import JsonResponse
import json
from rest_framework.response import Response
# from botometer import botometer.__init__
from botometer_python.botometer import *

from django.shortcuts import render_to_response

from .models import Twitterparse
# from .models import Tweet
from .serializers import TwitterparseSerializer
# from .serializers import TweetparseSerializer

from twitter_auth.utils import *
import tweepy
from tweepy.auth import OAuthHandler
import pprint

import pdb

# class TimeLineStatus():
#


class ListTwitterDataView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Twitterparse.objects.all()
    serializer_class = TwitterparseSerializer


# class ListTweetsView(generics.ListAPIView):
#     """
#     Provides a get method handler.
#     """
#     queryset = Tweet.objects.all()
#     serializer_class = TweetparseSerializer

def timeline(request):
    """
    display some user info to show we have authenticated successfully
    """
    # print(request)
    twitter_user = '@katjamfitz'
    # twitter_user = request['twitter_user']
    api = get_api(request)
    timeline = api.user_timeline(twitter_user, count=10)
    # profile_image_url_https =.profile_image_url_https()

    status_list = []
    for raw_status in timeline:
        print(raw_status)
        print("\n\n\n\n\n\n\n")
        status = {
            'id': raw_status.id,
            'text': raw_status.text,
            'profile_url': raw_status.user.profile_image_url_https
        }
        status_list.append(status)
    return JsonResponse(status_list, safe=False)
    # return render_to_response('timeline.html', {'timeline' : timeline})


    #pdb.set_trace()




    # print(timeline)
    # print(timeline[0]._json)
    # return render_to_response('timeline.html', {'timeline' : timeline})
    # return render_to_response('timeline.html', {'timeline' : timeline})

    # return timeline
    # print(timeline)
def check_account(request):
    CONSUMER_KEY = 'fdeOJrxMU7xE1KuflEQudxAg8'
    CONSUMER_SECRET = 'lGgJXT5sqGPEVPA4cvxZGuJk3HKPARZCsveptj1ihvbXE1YwT4'
    MASHAPE_KEY = 'JhMriAY1cBmshVq8nl7gPICau0ybp1CBgByjsniK45FLVHNZH2'

    twitter_user = '@' + request.GET.get('twitter_user', '')
    count = request.GET.get('count', 10)
    api = get_api(request)

    botometer = Botometer(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, mashape_key=MASHAPE_KEY)
    result = botometer.check_account(user=twitter_user);
    bot_result = {
        'screen_name': twitter_user,
        'bot_score': result['display_scores']['english'],
        'profile_url': result['user']['profile_url']
    }
    print(result)

    return JsonResponse(bot_result, safe=False)

# from .models import Tweet
def check_account_in(request):
    CONSUMER_KEY = 'fdeOJrxMU7xE1KuflEQudxAg8'
    CONSUMER_SECRET = 'lGgJXT5sqGPEVPA4cvxZGuJk3HKPARZCsveptj1ihvbXE1YwT4'
    MASHAPE_KEY = 'JhMriAY1cBmshVq8nl7gPICau0ybp1CBgByjsniK45FLVHNZH2'

    twitter_user = '@' + request.GET.get('twitter_user', '')
    count = request.GET.get('count', 10)
    api = get_api(request)

    accounts = []
    for friend in api.friends(twitter_user, count=count):
        accounts.append('@' + friend._json['screen_name'])

    botometer = Botometer(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, mashape_key=MASHAPE_KEY)
    bot_results = []
    for screen_name, result in botometer.check_accounts_in(accounts=accounts):
        bot_results.append({
            'screen_name': screen_name,
            'bot_score': result['display_scores']['english'],
            'profile_url': result['user']['profile_url']

        })
        print(result)
        print("\n\n\n\n\n\n\n\n\n\n")
    return JsonResponse(bot_results, safe=False)



# def user_tweets():
#     auth = OAuthHandler('Consumer Key', 'Consumer Secret')
#     auth.set_access_token('OAuth Access Token', 'OAuth Access Token Secret')
#     api = tweepy.API(auth)
#     user_tweets = api.user_timeline(count=50)
#     return JsonResponse(user_tweets[0]._json)
#
# def save_to_db():
#     original_tweets = user_tweets()
#     for original_tweet in original_tweets:
#         if not original_tweet.retweeted:
#             if not Tweet.objects.filter(tweet_id=original_tweet.id):
#                 new_tweet = Tweet(tweet_id = original_tweet.id, tweet_text = original_tweet.text, published_date = original_tweet.created_at, is_active = True)
#                 new_tweet.save()
#
# #@login_required
# def tweet_list(request):
#     tweets = Tweet.objects.order_by('-published_date')
#     page = request.GET.get('page', 1)
#     paginator = Paginator(tweets, 10)
#     try:
#         tweets = paginator.page(page)
#     except PageNotAnInteger:
#         tweets = paginator.page(1)
#     except EmptyPage:
#         tweets = paginator.page(paginator.num_pages)
#     return render(request, 'cms/timelinme.html', {'tweets': tweets})
# def analyzed_timeline(request):
#     """
#     display some user info to show we have authenticated successfully
#     """
#
#     api = get_api(request)
#     timeline = api.user_timeline('katjamfitz')
#     # analyzed_timeline = botapi.analyze(timeline)
#     # print(analyzed_timeline)
#
#     return render_to_response('timeline.html', {'timeline' : timeline})
