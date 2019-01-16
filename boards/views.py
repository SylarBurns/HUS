from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.core import serializers 

class ListView(generic.TemplateView):
    template_name = 'boards/boardList.html'

class DetailView(generic.TemplateView):
    template_name = 'boards/boardDetail.html'

class CreateView(generic.TemplateView):
    template_name = 'boards/boardCreate.html'

class UpdateView(generic.TemplateView):
    template_name = 'boards/boardRewrite.html'