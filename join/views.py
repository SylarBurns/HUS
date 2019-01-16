
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.core import serializers

class clauseView(generic.TemplateView):
    template_name = 'join/clause.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
class joinFormView(generic.TemplateView):
    template_name = 'join/joinForm.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context