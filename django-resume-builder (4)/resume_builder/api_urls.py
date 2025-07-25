from django.urls import path, include

# Simple API URLs - only if REST framework is available
try:
    from rest_framework.routers import DefaultRouter
    from . import api_views
    
    router = DefaultRouter()
    # Add your API viewsets here when needed
    
    urlpatterns = [
        path('', include(router.urls)),
    ]
except ImportError:
    urlpatterns = []
