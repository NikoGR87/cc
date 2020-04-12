# myauctionapi/serializers.py
 
from rest_framework import serializers 

from .models import Items

from .models import Auctions

from .models import ItemHistory

from .models import Bidding 
 
class ItemsSerializer(serializers.ModelSerializer):
   
   class Meta:
      
       model = Items
      
       fields = ('itemTitle','status','itemDescription','itemOwner')
       
class AuctionsSerializer(serializers.ModelSerializer): 
    
    class Meta:
    
        model = Auctions
        
        fields = ('auctionBiddingPrice', 'userBidding', 'auctionStatus', 'itemTitle') 

class ItemHistorySerializer(serializers.ModelSerializer): 
    
    class Meta: 
        
        model = ItemHistory 
        
        fields = ('itemTitle','finalPrice', 'itemDescription', 'itemBoughtFrom')
        
class BiddingSerializer(serializers.ModelSerializer):
   
   class Meta:
      
       model = Bidding
      
       fields = ('biddingPrice',)

        
