from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.models import User


from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status, viewsets, permissions

#from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import *
from .models import *



# Create your views here.
def index(request):
    return HttpResponse("Hello world!")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]
    #authentication_class = JSONWebTokenAuthentication

class ItemPledgeViewSet(viewsets.ModelViewSet):
    queryset = ItemPledge.objects.all()
    serializer_class = ItemPledgeSerializer
    #permission_classes = [permissions.IsAuthenticated]
    #authentication_class = JSONWebTokenAuthentication

class CampaignItemViewSet(viewsets.ModelViewSet):
    queryset = CampaignItem.objects.all()
    serializer_class = CampaignItemSerializer
    #permission_classes = [permissions.IsAuthenticated]
    #authentication_class = JSONWebTokenAuthentication

class CampaignGoalViewSet(viewsets.ModelViewSet):
    queryset = CampaignGoal.objects.all()
    serializer_class = CampaignGoalSerializer
    #permission_classes = [permissions.IsAuthenticated]
    #authentication_class = JSONWebTokenAuthentication

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    #permission_classes = [permissions.IsAuthenticated]
    #authentication_class = JSONWebTokenAuthentication
