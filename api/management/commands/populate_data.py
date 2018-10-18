import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from ...models import Handler, Tweets

from birdy.twitter import UserClient

CONSUMER_KEY = "cvIOqEVIgjHg7nWuXPCGntRrJ"

CONSUMER_SECRET = "jNTTgF0Ee4QisCbyeegFhU2Gj7j7L1jR5CQYzLemnOCdBcy7XR"  # (API secret key)


#   Access token & access token secret
ACCESS_TOKEN = "252358912-Ec7Q9BDkNycm1AA8nWqHMRyABV8ejQSwMuQIuayt" # (Access token)

ACCESS_TOKEN_SECRET = "bDZbaBmrtnJMQd5bgCAMXTAZoA5O66scTtxOO4vHhUJDK" #  (Access token secret)


client = UserClient(CONSUMER_KEY,
                    CONSUMER_SECRET,
                    ACCESS_TOKEN,
                    ACCESS_TOKEN_SECRET)
                    
def fetchData(twitter_handler):   
    """
    Fetch the twitter data and save it into the database
    """
    response = client.api.users.show.get(screen_name=twitter_handler)
    followers = response.data.get('followers_count',0)
    following = response.data.get('friends_count',0)
    k = {'twitterhandle':twitter_handler,'follower':followers, 'following': following}
    handler, created = Handler.objects.get_or_create(**k)
    handler.save() 
    print("twitter_handler: ",twitter_handler,"saved in DB")



class Command(BaseCommand):
    """
    dump twitter data from twitter api into Database
    """
    def handle(self, *args, **options):
        twitter_handler = ['netflix', 'hbo', 'hulu', 'disney', 'pepsi', 'katyperry', 'YouTube', 'NASA', 'Adele', 'elonmusk']
        for i in twitter_handler:
            fetchData(i)


