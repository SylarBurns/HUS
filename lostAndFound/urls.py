from django.urls import path

from .views import (
    listView,
    detailView,
    createView,
    updateView,
    deleteView,
)

app_name = 'lostAndFound'
urlpatterns = [
    # ex: /lostAndFound/
    path('', listView.as_view(), name='list'),

    # 리스트에서 lost만 정렬
    #path('lost/')

    # ex: /lostAndFound/5/
    path('<int:pk>/', detailView.as_view(), name='detail'),
    # ex: /lostAndFound/create/
    path('create/', createView.as_view(), name='create'),
    # ex: /lostAndFound/5/update/
    path('<int:pk>/update/', updateView.as_view(), name='update'),
    # ex: /lostAndFound/5/delete/
    path('<int:pk>/delete/', deleteView.as_view(), name='delete'),
]