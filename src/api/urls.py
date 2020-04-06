"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin

from django.urls import path, include # Added included

from rest_framework.routers import DefaultRouter 

from items.views import ItemsViewSet 

from auctions.views import AuctionsViewSet 

from bidding.views import BiddingViewSet 

from itemhistory.views import ItemHistoryViewSet 


router = DefaultRouter() 

router.register('items', ItemsViewSet)

router.register('auctions', AuctionsViewSet)

router.register('bidding', BiddingViewSet)

router.register('itemhistory', ItemHistoryViewSet)
 

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
    path('authentication/', include('users.urls')),
    
    path('v1/', include(router.urls)), # Version 1 of our API
]
