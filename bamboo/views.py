from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.urls import reverse
from heart.models import Post, PostRelation, User
from .forms import PostModelForm
from django.utils import timezone

class bambooListView(ListView):
    template_name = 'bamboo/boardList.html'
    queryset= Post.objects.all().filter(boardNum__exact=3).order_by('-pk')

class bambooDetailView(DetailView):
    template_name = 'bamboo/boardDetail.html'
    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Post, id=id_)


class bambooCreateView(CreateView):
    model = Post
    form_class = PostModelForm
    template_name = 'bamboo/boardCreate.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.boardNum = 3
        post.pubDate = timezone.now()
        post.save()
        postRelation= PostRelation(post=post, user=User.objects.get(pk=2), isWriter=True, annonimity=True, annoName="익명")
        postRelation.save()
        return redirect('bamboo:bambooDetail', pk=post.pk)


class bambooUpdateView(UpdateView):
    template_name = 'bamboo/boardCreate.html'
    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Post, id=id_)