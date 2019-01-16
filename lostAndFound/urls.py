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
    # ex: /lostAndFound/5/detail/
    path('detail/', detailView.as_view(), name='detail'),
    # ex: /lostAndFound/create/
    path('create/', createView.as_view(), name='create'),
    # ex: /lostAndFound/5/update/
    path('update/', updateView.as_view(), name='update'),
    # ex: /lostAndFound/5/delete/
    path('delete/', deleteView.as_view(), name='delete'),
]