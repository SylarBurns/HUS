from django.urls import path

from . import views
app_name = 'bamboo'
urlpatterns = [
    path('', views.bambooListView.as_view(), name='bambooList'),
    path('<int:pk>/', views.bambooDetailView.as_view(), name='bambooDetail'),
    path('create/', views.bambooCreateView.as_view(), name='bambooCreate'),
    # path('<int:pk>/rewrite/', views.bambooUpdateView.as_view(), name='bambooRewrite'),
]
