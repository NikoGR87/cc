from django.db import models

# Create your models here.

class Bidding(models.Model):

    biddingId = models.AutoField(primary_key=True)  #  Set ID as the primary key
    
    #auctionId = models.ForeignKey(
    #    'Auctions',
    #    on_delete=models.CASCADE,) 
    
    biddingPrice = models.IntegerField()