from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse


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
