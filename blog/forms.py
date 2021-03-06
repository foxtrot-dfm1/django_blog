from django import forms
from django.core.exceptions import ValidationError
from .models import Tag, Post

class TagForm(forms.ModelForm):
	# title = forms.CharField(max_length = 50)
	# slug = forms.CharField(max_length = 50)

	# title.widget.attrs.update({'class' : 'form-control'})
	# slug.widget.attrs.update({'class' : 'form-control'})

	class Meta:
		model = Tag
		fields = ['title', 'slug']

		widgets = {
			'title' : forms.TextInput(attrs = {'class' : 'form-control'}),
			'slug' : forms.TextInput(attrs = {'class' : 'form-control'})
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()
		
		if new_slug == 'create':
			raise ValidationError('Slug may not be "Create"')
		if Tag.objects.filter(slug__iexact = new_slug).count():
			raise ValidationError('Slug "{}" already exists'.format(new_slug))

		return new_slug

	# def save(self):
	# 	title = self.cleaned_data['title']
	# 	slug = self.cleaned_data['slug']
	# 	new_tag = Tag.objects.create(title  = title, slug = slug)
	# 	return new_tag


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'slug', 'body', 'tags']

		widgets = {
			'title' : forms.TextInput(attrs = {'class' : 'form-control'}),
			'slug' : forms.TextInput(attrs = {'class' : 'form-control'}),
			'tags' : forms.SelectMultiple(attrs = {'class' : 'form-control'}),
			'body;' : forms.TextInput(attrs = {'class' : 'form-control'}),
		}
	
	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()
		
		if new_slug == 'create':
			raise ValidationError('Slug may not be "Create"')
		if Tag.objects.filter(slug__iexact = new_slug).count():
			raise ValidationError('Slug "{}" already exists'.format(new_slug))

		return new_slug

