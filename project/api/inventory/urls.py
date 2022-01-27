from django.urls import path, re_path
from .views import *

# URLConf 
# for urls prefixed by /api/
urlpatterns = [
    path('inventory/', InventoryView.as_view()),
    re_path('inventory/(?P<name>.+)/$', InventoryView.as_view()),
]