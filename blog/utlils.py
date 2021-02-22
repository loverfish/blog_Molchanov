from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={
            self.model.__name__.lower(): obj,
            'admin_panel': obj,
            'detail': True,
        })


class ObjectCreateMixin:
    modelform = None
    template = None

    def get(self, request):
        form = self.modelform()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.modelform(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    modelform = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.modelform(instance=obj)
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'form': bound_form})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.modelform(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'form': bound_form})


class ObjectDeleteMixin:
    model = None
    template = None
    reverse_template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.reverse_template))


class ObjectDelMixin:
    model = None
    reverse_template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        name = self.model.__name__.lower()
        return render(request, 'blog/obj_del.html', context={'obj': obj, 'name': name})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.reverse_template))


def pagination(request, obj_list):
    paginator = Paginator(obj_list, 5)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'prev_url': prev_url,
        'next_url': next_url,
        'is_paginated': is_paginated,
    }
    return context
