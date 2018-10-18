from django.db import models

# Create your models here.

class Handler(models.Model):
    """
    Twitter Handler model : model for Twitter user
    """
    twitterhandle = models.CharField(max_length=100,primary_key=True)
    follower = models.IntegerField()
    following = models.IntegerField()
    tweets = models.ForeignKey("Tweets",on_delete=models.CASCADE, default=None, blank=True,null=True)
   
    class Meta:
        verbose_name = "Handler"

    def __str__(self):
        return self.twitterhandle

class Tweets(models.Model):
    """
    Tweets models
    """
    id = models.CharField(max_length=100,primary_key=True)
    tweet = models.CharField(max_length=280)
    created_date = models.DateTimeField()
    retweets = models.IntegerField(default=0)
    
    def __str__(self):
        return self.tweet
    