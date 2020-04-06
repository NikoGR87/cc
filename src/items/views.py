from rest_framework import viewsets 

from .models import Items

from .serializers import ItemsSerializer 

class ItemsViewSet(viewsets.ModelViewSet):
    
    queryset = Items.objects.all().order_by('itemTitle')
    
    serializer_class = ItemsSerializer 
