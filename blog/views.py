from django.shortcuts import render
from django.views.generic import View

from .models import Post, Tag
from .forms import TagForm, PostForm
from .utlils import ObjectDetailMixin, ObjectCreateMixin


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class PostCreate(ObjectCreateMixin, View):
    modelform = PostForm
    template = 'blog/post_create.html'


class TagCreate(ObjectCreateMixin, View):
    modelform = TagForm
    template = 'blog/tag_create.html'


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'blog/tag_detail.html', context={'tag': tag})

# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog/post_detail.html', context={'post': post})
