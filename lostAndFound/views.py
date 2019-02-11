from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.urls import reverse
from django.utils import timezone
from .forms import lostAndFoundPostModelForm
from heart.models import (
    Post,
    PostRelation,
    User
)

class listView(ListView):
    template_name = 'lostAndFound/list.html'
    queryset = Post.objects.all().filter(boardNum__exact=6).order_by('-pk')


class detailView(DetailView):
    template_name = 'lostAndFound/detail.html'
    
    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Post, id=id_)


class createView(CreateView):
    model = Post
    form_class = lostAndFoundPostModelForm
    template_name = 'lostAndFound/create.html'

    def form_valid(self,form):
        post = form.save(commit=False)
        post.boardNum = 6
        post.pubDate = timezone.now()
        post.hitCount = 0  
        if post.boardType == 'Lost':
            post.status='Lost'
        else :
            post.status='Found'      
        post.save()
        postRelation = PostRelation(post=post, user=User.objects.get(pk=1))
        postRelation.save()
        return redirect('lostAndFound:detail', pk=post.pk)



class updateView(UpdateView):
    model = Post
    form_class = lostAndFoundPostModelForm
    template_name = 'lostAndFound/update.html'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Post, id=id_)
    
    def form_valid(self,form):
        return super().form_valid(form)    


class deleteView(TemplateView):
    template_name = 'lostAndFound/delete.html'