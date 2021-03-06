from django.shortcuts import render, get_object_or_404
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.urls import reverse
from django.core import serializers

class mainPageView(TemplateView):
    template_name='mainPage/mainPageTemplate.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['range']=[1,2,3,4]
        return context

class basePageView(TemplateView):
    template_name='mainpage/basePage.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['range']=[1,2,3,4]
        context['ten']=[1,2,3,4,5,6,7,8,9,10]
        return context

class testPageView(TemplateView):
    template_name="mainPage/test.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['range']=[1,2,3,4]
        context['ten']=[1,2,3,4,5,6,7,8,9,10]
        return context
    
