from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("pk","url", "username", "email")


class ItemPledgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemPledge
        fields = ("pk", "url", "user", "item", "pledged_dt", "fulfilled", "pledged_amt")


class CampaignItemSerializer(serializers.HyperlinkedModelSerializer):
    pledges = ItemPledgeSerializer(many=True)

    class Meta:
        model = CampaignItem
        fields = ("pk", "url", "campaign", "name", "desc", "target_amount", "pledges")


class CampaignGoalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CampaignGoal
        fields = ("pk", "url", "campaign", "goal_amt")

class CampaignSerializer(serializers.HyperlinkedModelSerializer):
    items = CampaignItemSerializer

    class Meta:
        model = Campaign
        fields = ("pk", "url", "name", "desc"
                    "start_dt", "end_dt", "event_dt")
