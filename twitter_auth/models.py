from django.db import models


class Twitter_Auth(models.Model):
    # song title
    twitter_id = models.BigIntegerField(max_length=255, null=False)
    # id of twitter user
    name = models.CharField(max_length=255, null=False)
    # name
    screen_name = models.CharField(max_length=255, null=False)
    #twitter screen name may differ from name (use as db index?)

    # screen_name = models.CharField(max_length=255, null=False)
    # #twitter screen name may differ from name (use as db index?)
    #
    # screen_name = models.CharField(max_length=255, null=False)
    # #twitter screen name may differ from name (use as db index?)
    def __str__(self):
        return "{} - {}".format(self.twitter_id, self.name, self.screen_name)
