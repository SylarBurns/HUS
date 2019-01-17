from django.contrib import admin
from .models import User, Post, Comment, File, PostRelation, ComRelation
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(File)
admin.site.register(PostRelation)
admin.site.register(ComRelation)
# Register your models here.
