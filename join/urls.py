from django.urls import path
from . import views
app_name = 'join'
urlpatterns = [
    path('', views.clauseView.as_view(), name='clause'),
    path('joinForm/', views.joinFormView.as_view(), name='joinForm'),
]