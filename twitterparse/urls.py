from django.conf.urls import *
from django.urls import path
# from .models import Tweet
from .views import ListTwitterDataView
# from .views import ListTweetsView

from . import views

urlpatterns = [
    path('TwitterDataView/', ListTwitterDataView.as_view()),
    path('', ListTwitterDataView.as_view()),
    url(r'^timeline/$', views.timeline, name='timeline'),
    url(r'^check_account/$', views.check_account, name='check_account'),
    url(r'^check_account_in/$', views.check_account_in, name='check_account_in')
    # url(r'^tweets/$', views.timeline, name='tweets'),
    # path('ListTweetsView', ListTweetsView.as_view()),
    # path('', ListTweetsView.as_view()),
    # url(r'^tweets/$', views.tweets, name='tweets'),
    # url(r'^analyzed_timeline/$', views.analyzed_timeline, name='analyzed_timeline'),
]
