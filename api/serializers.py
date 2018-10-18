from rest_framework import serializers
from .models import Handler, Tweets


class TweetsSerializer(serializers.ModelSerializer):
    """
    Serializer for Tweets model
    """
    class Meta:
        model = Tweets
        fields = '__all__'


class HandlerSerializer(serializers.ModelSerializer):
    """
    Serializer for Handler model
    """
    tweets = TweetsSerializer(many=True)

    class Meta:
        model = Handler
        fields = ('twitterhandle', 'follower', 'following', 'tweets')
        
class DayWiseTweetSerializer(serializers.Serializer):
    """DayWiseTweetSerializer to store number of tweets on each day."""
    monday = serializers.IntegerField()
    tuesday = serializers.IntegerField()
    wednesday = serializers.IntegerField()
    thrusday = serializers.IntegerField()
    friday = serializers.IntegerField()
    saturday = serializers.IntegerField()
    sunday = serializers.IntegerField()