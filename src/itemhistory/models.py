from django.db import models

# Create your models here.

class ItemHistory(models.Model):

    ItemId = models.AutoField(primary_key=True)  #  Set ID as the primary key

    itemTitle = models.CharField(max_length=60)
    
    finalPrice = models.IntegerField()
    
    itemDescription = models.CharField(max_length=60)
    
    itemBoughtFrom = models.CharField(max_length=60)
    
    def __str__(self):        
        return self.name