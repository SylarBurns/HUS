from django.urls import path
from .views import (
    mainPageView,
    basePageView,
    testPageView,
)
app_name = 'mainPage'
urlpatterns = [
    path('', mainPageView.as_view(), name='mainPage'),
    path('base/', basePageView.as_view(), name="basepage" ),
    path('test/', testPageView.as_view(), name="testPage"),
]