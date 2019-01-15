from rest_framework import generics
from django.http import JsonResponse
import json
from rest_framework.response import Response

from django.shortcuts import render_to_response

from .models import Twitterparse
# from .models import Tweet
from .serializers import TwitterparseSerializer
# from .serializers import TweetparseSerializer

from twitter_auth.utils import *
import tweepy
from tweepy.auth import OAuthHandler



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
    print(request)
    twitter_user = 'katjamfitz'
    # twitter_user = request['twitter_user']
    api = get_api(request)
    timeline = api.user_timeline(twitter_user, count=10)
    new_timeline = {"tweets":timeline}

    # import pdb; pdb.set_trace();

    # print(timeline)
    # print(timeline[0]._json)
    # return render_to_response('timeline.html', {'timeline' : timeline})
    # return render_to_response('timeline.html', {'timeline' : timeline})

    # return timeline
    # print(timeline)
    return JsonResponse(timeline[0]._json)
    # return render_to_response('timeline.html', {'timeline' : timeline})

# from .models import Tweet




def user_tweets():
    auth = OAuthHandler('Consumer Key', 'Consumer Secret')
    auth.set_access_token('OAuth Access Token', 'OAuth Access Token Secret')
    api = tweepy.API(auth)
    user_tweets = api.user_timeline(count=50)
    return JsonResponse(user_tweets[0]._json)

def save_to_db():
    original_tweets = user_tweets()
    for original_tweet in original_tweets:
        if not original_tweet.retweeted:
            if not Tweet.objects.filter(tweet_id=original_tweet.id):
                new_tweet = Tweet(tweet_id = original_tweet.id, tweet_text = original_tweet.text, published_date = original_tweet.created_at, is_active = True)
                new_tweet.save()

#@login_required
def tweet_list(request):
    tweets = Tweet.objects.order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(tweets, 10)
    try:
        tweets = paginator.page(page)
    except PageNotAnInteger:
        tweets = paginator.page(1)
    except EmptyPage:
        tweets = paginator.page(paginator.num_pages)
    return render(request, 'cms/timelinme.html', {'tweets': tweets})
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
