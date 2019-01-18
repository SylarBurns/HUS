from django.urls import path

from . import views
app_name = 'skyLake'
urlpatterns = [
    path('', views.skyLakeListView.as_view(), name='skyLakeList'),
    path('<int:pk>/', views.skyLakeDetailView.as_view(), name='skyLakeDetail'),
    path('create/', views.skyLakeCreateView.as_view(), name='skyLakeCreate'),
    # path('<int:pk>/rewrite/', views.skyLakeUpdateView.as_view(), name='skyLakeRewrite'),
]
