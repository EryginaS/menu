from django.urls import path

from .views import PositionsListView, OrderView

app_name = 'position'

urlpatterns = [
    path('', PositionsListView.as_view(), name='index'),
    path('order/', OrderView.as_view(), name='order'),
]