from rest_framework import serializers
from .models import Twitterparse
# from .models import Tweet


class TwitterparseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Twitterparse
        fields = ("created_at","tweet_id", "text", "published_date", "is_active")
