from rest_framework import viewsets
 
from .models import Bidding
 
from .serializers import BiddingSerializer 

class BiddingViewSet(viewsets.ModelViewSet): 
    
    queryset = Bidding.objects.all() 
    
    serializer_class = BiddingSerializer
