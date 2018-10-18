import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from ...models import Handler, Tweets

from birdy.twitter import UserClient

"""""
Add own keys from twitter to access their apis
"""
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
    try:
        handler, created = Handler.objects.get_or_create(**k)
        print("created",created)
        # handler.save() 
        print("twitter_handler: ",twitter_handler,"saved in DB")
    except Exception as ex:
        print(ex)
    



class Command(BaseCommand):
    """
    dump twitter data from twitter api into Database
    """
    def handle(self, *args, **options):
        twitter_handler = ['netflix', 'hbo', 'hulu', 'disney', 'pepsi', 'katyperry', 'YouTube', 'NASA', 'Adele', 'elonmusk']
        for i in twitter_handler:
            fetchData(i)


