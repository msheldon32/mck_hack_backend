from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Campaign)
admin.site.register(CampaignItem)
admin.site.register(ItemPledge)
admin.site.register(CampaignGoal)