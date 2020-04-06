from rest_framework import viewsets
 
from .models import ItemHistory
 
from .serializers import ItemHistorySerializer 

class ItemHistoryViewSet(viewsets.ModelViewSet): 
    
    queryset = ItemHistory.objects.all() 
    
    serializer_class = ItemHistorySerializer
