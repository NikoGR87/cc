from django.db import models

# Create your models here.

from django.core import validators

from django.core.exceptions import ValidationError

STATUS_CHOICES = ( # Specifying choices
    	("1", 'New'), 
    	("2", 'Used'),  
    )
    
STATUS_AUCTIONS_CHOICES = ( # Specifying choices
    	("1", 'Open'), 
    	("2", 'Completed'),  
    )

class Items(models.Model): 

    itemId = models.AutoField(primary_key=True)  #  Set ID as the primary key 

    itemTitle = models.CharField(max_length=60)

    timeStamp = models.DateTimeField
 
    status = models.CharField( 
        max_length = 20, 
        choices = STATUS_CHOICES, 
        default = '1'
        )

    itemDescription = models.CharField(max_length=60)
    
    auctionExpirationTime = models.DateTimeField

    itemOwner = models.CharField(max_length=60)
    

class Auctions(models.Model): 
        
    auctionId = models.AutoField(primary_key=True)  #  Set ID as the primary key
    
    auctionBiddingPrice = models.IntegerField()
    
    userBidding = models.CharField(max_length=60, default='')
    
    auctionStatus = models.CharField( 
        max_length = 20, 
        choices = STATUS_AUCTIONS_CHOICES, 
        default = '1'
        )
        
    #timeLeftToComplete =     

    auctionWinner = models.CharField(max_length=60)
    
    #itemId = models.ForeignKey(Items, on_delete=models.CASCADE) 
    
    itemTitle = models.CharField(max_length=60, default='') 

    #def __str__(self):        
        #return self.name

class ItemHistory(models.Model):

    ItemId = models.AutoField(primary_key=True)  #  Set ID as the primary key

    itemTitle = models.CharField(max_length=60)

    finalPrice = models.IntegerField()

    itemDescription = models.CharField(max_length=60)

    itemBoughtFrom = models.CharField(max_length=60)
    
class Bidding(models.Model):

    biddingId = models.AutoField(primary_key=True)  #  Set ID as the primary key
    
    auctionId = models.ForeignKey(Auctions,on_delete=models.CASCADE,) 
    
    biddingPrice = models.IntegerField()
    
    biddingWinner = models.CharField(max_length=60, default='')
   
    
