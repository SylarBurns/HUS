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

class skyLakeListView(ListView):
    template_name = 'skyLake/boardList.html'
    queryset= Post.objects.all().filter(boardNum__exact=2).order_by('-pk')

class skyLakeDetailView(DetailView):
    template_name = 'skyLake/boardDetail.html'
    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Post, id=id_)


class skyLakeCreateView(CreateView):
    model = Post
    form_class = PostModelForm
    template_name = 'skyLake/boardCreate.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.boardNum = 2
        post.pubDate = timezone.now()
        post.save()
        postRelation= PostRelation(post=post, user=User.objects.get(pk=2), isWriter=True)
        postRelation.save()
        return redirect('skyLake:skyLakeDetail', pk=post.pk)


# class skyLakeUpdateView(UpdateView):
#     template_name = 'skyLake/boardRewrite.html'
#     def get_object(self):
#         id_ = self.kwargs.get("pk")
#         return get_object_or_404(Post, id=id_)