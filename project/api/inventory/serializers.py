from rest_framework import serializers
from inventory.models import * # import the Inventory and Supplier models 

#serializer for Inventory model
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

#serializer for Supplier model
class SupplierSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Supplier
        fields = '__all__'
