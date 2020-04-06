from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
 
from .models import Auctions
 
from .serializers import AuctionsSerializer 

class AuctionsViewSet(viewsets.ModelViewSet): 
    
    queryset = Auctions.objects.all() 
    
    serializer_class = AuctionsSerializer
