from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListView.as_view(), name='list'),
    path('detail/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('rewrite/', views.UpdateView.as_view(), name='rewrite'),
]
