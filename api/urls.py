from django.urls import path
from .views import *


urlpatterns = [
    path("follower/", FollowerView.as_view(), name='follower'),
    path("following/", FollowingView.as_view(), name='following'),
    path("toptweets/", ToptweetsView.as_view(), name='toptweets'),
    # path("savetweetcount/", IndexView.as_view(), name='index'),
    # path("tweettrends/", IndexView.as_view(), name='index'),
    path("", HandlerData.as_view(), name='index'),
]
