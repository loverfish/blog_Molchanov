from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

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
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()
    context = pagination(request, posts)

    return render(request, 'blog/home.html', context=context)


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    posts = tag.posts.all()
    context = {'tag': tag, **pagination(request, posts)}

    return render(request, 'blog/tag_pag.html', context=context)

# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog/post_detail.html', context={'post': post})
