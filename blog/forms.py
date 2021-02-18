from django import forms
from django.core.exceptions import ValidationError
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('slug can not be "create"')
        return new_slug


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('slug can not be "create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('"{}" slug is already exist'.format(new_slug))
        return new_slug


    # title = forms.CharField(max_length=50)
    # slug = forms.SlugField(max_length=50)
    # title.widget.attrs.update({'class': 'form-control'})
    # slug.widget.attrs.update({'class': 'form-control'})

    # def save(self):
    #     new_tag = Tag.objects.create(
    #         title=self.cleaned_data['title'],
    #         slug=self.cleaned_data['slug'],
    #     )
    #     return new_tag
