from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class ItemPledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPledge
        fields = ("pk", "url", "user", "item", "pledged_dt", "fulfilled", "pledged_amt")


class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = ("pk","url", "campaign", "user")


class UserSerializer(serializers.ModelSerializer):
    subscriptions = UserSubscriptionSerializer(source="subscription_user", many=True)

    class Meta:
        model = User
        fields = ("pk","url", "username", "email", "subscriptions")

class CampaignItemSerializer(serializers.ModelSerializer):
    pledges = ItemPledgeSerializer(source="pledge_item", many=True)

    class Meta:
        model = CampaignItem
        fields = ("pk", "url", "campaign", "name", "desc", "target_amt", "pledges")


class CampaignGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignGoal
        fields = ("pk", "url", "campaign", "goal_amt")

class CampaignSerializer(serializers.ModelSerializer):
    items = CampaignItemSerializer(source="item_campaign", many=True)

    class Meta:
        model = Campaign
        fields = ("pk", "url", "name", "desc",
                    "start_dt", "end_dt", "event_dt", "items")
