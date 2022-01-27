from django.shortcuts import render
from api.inventory.views import *
# Create your views here.

# view to display the full list of items in inventory
def display_list(request):
    context = {} # dictionary for initial data with field names as keys

    # add the dictionary during initialization
    context["dataset"] = FullInv.get_queryset(FullInv.as_view) # InventoryView is from api/inventory/views - api endpoint
    return render(request, "list_view.html", context) 

# view to display an inventory item based on its id
def item_details(request, id):
    dict = FullInv.get_queryset(FullInv.as_view).get(id=id)
    return render(request, "single_item.html", {'item': dict})