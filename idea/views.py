from idea.models import Idea
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from .models import Idea
# from .forms import IdeaForm


def idea(request):
    idea = Idea.objects.all()
    return render(request, 'idea.html', {'all_idea': idea})
