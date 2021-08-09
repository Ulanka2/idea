from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Idea, Author



class IdeaForm(forms.ModelForm):

    class Meta:
        model = Idea
        fields = ('title', 'text', 'img', 'author')

        widgets = {
        'title': forms.TextInput(attrs={'class':'form-control'}),
        'text': forms.Textarea(attrs={'class':'form-control'}),
        'img': forms.URLInput(attrs={'class':'form-control'}),
        }

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('name',)
 
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }