#in here, map urls to view function
from django.urls import path, re_path
from . import views 

# URLConf 
# for urls prefixed by inventory/

urlpatterns = [
    path('', views.display_list, name="full-list"), 
    re_path('(?P<id>[\d-]+)', views.item_details, name="single-item"),
]