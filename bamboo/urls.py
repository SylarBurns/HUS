from django.urls import path

from . import views
from heart.views import postLike, postDislike
app_name = 'bamboo'
urlpatterns = [
    path('', views.bambooListView.as_view(), name='bambooList'),
    path('<int:pk>/', views.bambooDetailView.as_view(), name='bambooDetail'),
    path('create/', views.bambooCreateView.as_view(), name='bambooCreate'),
    path('<int:pk>/like/', postLike, name="postLike"),
    path('<int:pk>/disLike/', postDislike, name="postDislike"),
    # path('<int:pk>/rewrite/', views.bambooUpdateView.as_view(), name='bambooRewrite'),
]
