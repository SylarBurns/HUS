from django.urls import path

from . import views
from .views import (
	MarketListView,
)
urlpatterns = [
	path('', MarketListView.as_view(), name='list'),
	
]
