from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import(
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView,
	TemplateView
)

class MarketListView(TemplateView):
    template_name = 'market/marketList.html'
