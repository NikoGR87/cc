from django.db import models

# Create your models here.

STATUS_CHOICES = ( # Specifying choices
    	("1", 'New'), 
    	("2", 'Used'),  
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
 
    def __str__(self):        
        return self.name
