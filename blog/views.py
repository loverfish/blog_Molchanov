from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Tag
from .forms import TagForm, PostForm
from .utlils import *


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    modelform = PostForm
    template = 'blog/post_create.html'
    raise_exception = True


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    modelform = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    modelform = PostForm
    template = 'blog/post_update.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    modelform = TagForm
    template = 'blog/tag_update.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    reverse_template = 'posts_list_url'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    reverse_template = 'tags_list_url'
    raise_exception = True


class PostDel(LoginRequiredMixin, ObjectDelMixin, View):
    model = Post
    reverse_template = 'posts_list_url'
    raise_exception = True


class TagDel(LoginRequiredMixin, ObjectDelMixin, View):
    model = Tag
    reverse_template = 'tags_list_url'
    raise_exception = True


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
