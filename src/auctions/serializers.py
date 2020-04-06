from rest_framework import serializers 

from .models import Auctions 
 
class AuctionsSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Auctions 
        fields = ('auctionBiddingPrice', 'auctionStatus', 'auctionWinner')