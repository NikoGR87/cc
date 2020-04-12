# Generated by Django 3.0.2 on 2020-04-06 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_itemhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bidding',
            fields=[
                ('biddingId', models.AutoField(primary_key=True, serialize=False)),
                ('biddingPrice', models.IntegerField()),
                ('biddingWinner', models.CharField(default='', max_length=60)),
                ('auctionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Auctions')),
            ],
        ),
    ]
