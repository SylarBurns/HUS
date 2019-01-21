from django import forms
from django.forms import ModelForm
from heart.models import Post
from heart.models import PostRelation

class PostModelForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
