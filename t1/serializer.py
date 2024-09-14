from rest_framework import serializers
from .models import Items,store

class Itemserializer(serializers.ModelSerializer):
    
    class Meta:
        model=Items
        fields="__all__"
        depth = 1
        
class storeserializer(serializers.ModelSerializer):
    
    items=Itemserializer(many=True,read_only=True)
    class Meta:
        model=store
        fields="__all__"