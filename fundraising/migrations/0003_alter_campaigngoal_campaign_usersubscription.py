# Generated by Django 4.1.1 on 2022-09-24 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0002_rename_fullfilled_itempledge_fulfilled_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaigngoal',
            name='campaign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='goal_campaign', to='fundraising.campaign'),
        ),
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='subscription_campaign', to='fundraising.campaign')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='subscription_user', to='fundraising.campaign')),
            ],
        ),
    ]
