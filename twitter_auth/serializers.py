from rest_framework import serializers
from .models import Twitter_Auth


class Twitter_AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Twitter_Auth
        fields = ("id", "name", "screen_name")
