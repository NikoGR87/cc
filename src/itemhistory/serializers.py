from rest_framework import serializers 

from .models import ItemHistory 
 
class ItemHistorySerializer(serializers.ModelSerializer): 
    
    class Meta: 
        
        model = ItemHistory 
        
        fields = ('itemTitle','finalPrice', 'itemDescription', 'itemBoughtFrom')
