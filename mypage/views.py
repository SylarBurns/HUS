from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.core import serializers

class myPostView(generic.TemplateView):
    template_name = 'mypage/myPost.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class myCommentView(generic.TemplateView):
    template_name = 'mypage/myComment.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class myDataView(generic.TemplateView):
    template_name = 'mypage/myData.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
class myReportView(generic.TemplateView):
    template_name = 'mypage/myReport.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
class myReportPopupView(generic.TemplateView):
    template_name = 'mypage/myReportPopup.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

