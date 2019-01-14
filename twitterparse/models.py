from django.db import models


class Twitterparse(models.Model):
    # song title
    tweet_id = models.BigIntegerField(max_length=255, null=False)
    # id of twitter user
    text = models.CharField(max_length=255, null=False)
    published_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    # name
    # screen_name = models.CharField(max_length=255, null=False)
    #twitter screen name may differ from name (use as db index?)

    # screen_name = models.CharField(max_length=255, null=False)
    # #twitter screen name may differ from name (use as db index?)
    #
    # screen_name = models.CharField(max_length=255, null=False)
    # #twitter screen name may differ from name (use as db index?)
    def __str__(self):
        return "{} - {}".format(self.tweet_id, self.text, self.published_date, self.is_active)

# class Tweet(models.Model):
#     tweet_id = models.CharField(max_length=250, null=True, blank=True)
#     tweet_text = models.TextField()
#     published_date = models.DateTimeField(blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     def __str__(self):
#         return self.tweet_text
