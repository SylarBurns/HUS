from django.urls import path
from .views import (
    mainPageView,
)
app_name = 'mainPage'
urlpatterns = [
    path('', mainPageView.as_view(), name='mainPage'),
]