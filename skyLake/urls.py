from django.urls import path

from . import views
from heart.views import postLike, postDislike

app_name = 'skyLake'
urlpatterns = [
    path('', views.skyLakeListView.as_view(), name='skyLakeList'),
    path('<int:pk>/', views.skyLakeDetailView.as_view(), name='skyLakeDetail'),
    path('create/', views.skyLakeCreateView.as_view(), name='skyLakeCreate'),
    path('<int:pk>/like/', postLike, name="postLike"),
    path('<int:pk>/disLike/', postDislike, name="postDislike"),
    # path('<int:pk>/rewrite/', views.skyLakeUpdateView.as_view(), name='skyLakeRewrite'),
]
