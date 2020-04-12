from rest_framework import viewsets 

from .models import Items

from .serializers import ItemsSerializer

from .models import Auctions
 
from .serializers import AuctionsSerializer

from .models import ItemHistory 

from .serializers import ItemHistorySerializer 

from .models import Bidding
 
from .serializers import BiddingSerializer 

class ItemsViewSet(viewsets.ModelViewSet):
    
    queryset = Items.objects.all().order_by('itemTitle')
    
    serializer_class = ItemsSerializer

class AuctionsViewSet(viewsets.ModelViewSet): 
    
    queryset = Auctions.objects.all() 
    
    serializer_class = AuctionsSerializer   

class ItemHistoryViewSet(viewsets.ModelViewSet): 
    
    queryset = ItemHistory.objects.all() 
    
    serializer_class = ItemHistorySerializer

class BiddingViewSet(viewsets.ModelViewSet): 
    
    queryset = Bidding.objects.all() 
    
    serializer_class = BiddingSerializer    
