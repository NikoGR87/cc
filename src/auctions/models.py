from django.db import models

# Create your models here.

STATUS_CHOICES = ( # Specifying choices
    	("1", 'Open'), 
    	("2", 'Completed'),  
    )

class Auctions(models.Model): 

    auctionId = models.AutoField(primary_key=True)  #  Set ID as the primary key
    
    auctionBiddingPrice = models.IntegerField()
    
    #user =  

    auctionStatus = models.CharField( 
        max_length = 20, 
        choices = STATUS_CHOICES, 
        default = '1'
        )

    #timeLeft 

    auctionWinner = models.CharField(max_length=60)
    
    #itemId = 
    
    def __str__(self):        
        return self.name