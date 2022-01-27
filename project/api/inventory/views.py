    
from rest_framework import generics
from api.inventory.serializers import *

# this is the api endpoint

# return selected objects based on URL query parameter (name only)
class InventoryView(generics.ListAPIView):
    serializer_class = InventorySerializer
    
    def get_queryset(self):
        queryset = Inventory.objects.all() #obtain all the objects stored first
        
        if (self.request.GET.get('name')): 
            prod_name = self.request.GET.get('name') # get the name of the inventory from the URL query parameter
            queryset = Inventory.objects.filter(inv_name=prod_name) #filter the objects based on the URL query parameter
        return queryset


#return all the objects in the Inventory model
class FullInv(generics.ListAPIView):
    serializer_class = InventorySerializer

    def get_queryset(self):
        queryset = Inventory.objects.all() #obtain all the objects stored in the model
        return queryset



