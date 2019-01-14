from django.urls import path
from .views import (
    mainPageView,
    basePageView,
)
app_name = 'mainPage'
urlpatterns = [
    path('', mainPageView.as_view(), name='mainPage'),
    path('base/', basePageView.as_view(), name="basepage" ),
]