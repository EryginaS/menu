from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import ApiPositionViewSet


urlpatterns = [
    path('position/', ApiPositionViewSet.as_view(), name="create_position"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
 ]