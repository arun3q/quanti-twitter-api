from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Handler
from .serializers import HandlerSerializer


class FollowerView(APIView):
    """
    API view for searching follower for a given Twitter Handler
    """
    allowed_methods = ['GET']
    serializer_class = HandlerSerializer

    def get(self, request, *args, **kwargs):
        follower = 0
        twitterhandle = request.query_params.get('twitterhandle', None)
        if twitterhandle is not None:
            follower = Handler.objects.filter(twitterhandle__icontains=twitterhandle)[0].follower
            
        return Response({"name":twitterhandle,"follower":follower}, status=status.HTTP_200_OK)
        
class FollowingView(APIView):
    """
    API view for searching follower for a given Twitter Handler
    """
    allowed_methods = ['GET']
    serializer_class = HandlerSerializer

    def get(self, request, *args, **kwargs):
        following = 0
        twitterhandle = request.query_params.get('twitterhandle', None)
        if twitterhandle is not None:
            following = Handler.objects.filter(twitterhandle__icontains=twitterhandle)[0].following
            
        return Response({"name":twitterhandle,"following":following}, status=status.HTTP_200_OK)    

        
class ToptweetsView(APIView):
    """
    API view for searching follower for a given Twitter Handler
    """
    allowed_methods = ['GET']
    serializer_class = HandlerSerializer

    def get(self, request, *args, **kwargs):
        following = 0
        twitterhandle = request.query_params.get('twitterhandle', None)
        if twitterhandle is not None:
            following = Handler.objects.filter(twitterhandle__icontains=twitterhandle)[0].following
            
        return Response({"name":twitterhandle,"toptweets":following}, status=status.HTTP_200_OK)            

class HandlerData(APIView):
    """
    API view for give all data of a Twitter Handler
    """
    allowed_methods = ['GET']
    serializer_class = HandlerSerializer
    # ('twitterhandle', 'follower', 'following', 'tweets')
    def get(self, request, *args, **kwargs):
        queryset = None

        twitterhandle = request.query_params.get('name', None)
        if twitterhandle is not None:
            queryset = Handler.objects.filter(twitterhandle__icontains=twitterhandle)
        else:
            queryset = Handler.objects.all()

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)        