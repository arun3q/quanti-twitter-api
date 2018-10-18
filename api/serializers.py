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