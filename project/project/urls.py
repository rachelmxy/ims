"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# sources: https://www.youtube.com/watch?v=LAIVhl2CG8E&ab_channel=TheNetNinja

from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.conf.urls.static import static
from django.conf import settings
from .views import * 

urlpatterns = [
    path('', display_home), # display home is from the views file
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')), 
    path('api/', include('api.inventory.urls')),
]

# source: https://www.youtube.com/watch?v=LAIVhl2CG8E&ab_channel=TheNetNinja
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)