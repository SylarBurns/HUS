from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

class listView(TemplateView):
    template_name = 'lostAndFound/list.html'

class detailView(TemplateView):
    template_name = 'lostAndFound/detail.html'

class createView(TemplateView):
    template_name = 'lostAndFound/create.html'

class updateView(TemplateView):
    template_name = 'lostAndFound/update.html'

class deleteView(TemplateView):
    template_name = 'lostAndFound/delete.html'