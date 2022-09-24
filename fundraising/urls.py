from django.urls import include, path

from .views import *
from rest_framework import routers


fundraising_router = routers.DefaultRouter()
fundraising_router.register(r'user', UserViewSet)
fundraising_router.register(r'item_pledge', ItemPledgeViewSet)
fundraising_router.register(r'campaign_item', CampaignItemViewSet)
fundraising_router.register(r'campaign_goal', CampaignGoalViewSet)
fundraising_router.register(r'campaign', CampaignViewSet)
fundraising_router.register(r'subscription', UserSubscriptionViewSet)


urlpatterns = [
    path('', include(fundraising_router.urls), name='index'),
]