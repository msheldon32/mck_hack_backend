from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Campaign(models.Model):
    name = models.CharField(max_length=64, null=False)
    desc = models.CharField(max_length=256, null=True)

    start_dt = models.DateTimeField()
    end_dt = models.DateTimeField()
    event_dt = models.DateTimeField()


class CampaignItem(models.Model):
    name = models.CharField(max_length=64, null=False)
    desc = models.CharField(max_length=256, null=True)

    target_amt = models.DecimalField(decimal_places=2, max_digits=16, null=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.RESTRICT, null=True, related_name="item_campaign")


class ItemPledge(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, related_name="pledge_user")
    item = models.ForeignKey(CampaignItem, on_delete=models.RESTRICT, null=True, related_name="pledge_item")

    pledged_dt = models.DateTimeField()
    fulfilled = models.BooleanField()

    pledged_amt = models.DecimalField(decimal_places=2, max_digits=16, null=True)

class CampaignGoal(models.Model):
    name = models.CharField(max_length=64, null=False)
    desc = models.CharField(max_length=256, null=True)

    goal_amt = models.DecimalField(decimal_places=2, max_digits=16, null=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.RESTRICT, null=True)