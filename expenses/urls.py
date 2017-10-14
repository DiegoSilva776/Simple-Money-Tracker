from django.conf.urls import url
from django.conf.urls import include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

from expenses import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'expenses', views.ExpenseViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
