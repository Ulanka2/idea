from idea.models import Author, Idea
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from .forms import AuthorForm, IdeaForm


def idea(request):
    idea = Idea.objects.all()
    author = Author.objects.all()
    return render(request, 'idea/idea.html', {'idea': idea, 'author': author})

def idea_detail(request, pk):
    idea_detail = get_object_or_404(Idea, pk=pk)
    return render(request, 
                'idea/idea_detail.html', 
                {'idea_detail': idea_detail,})

def add_idea(request):
    if request.method == "POST":
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm()
    return render(request, 'idea/idea_edit.html', {'form': form})

def idea_edit(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == "POST":
        form = IdeaForm(request.POST, instance=idea)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'idea/idea_edit.html', {'form': form})

def idea_delete(request, pk):
    try:
        idea = Idea.objects.get(id=pk)
        idea.delete()
        return redirect('idea')
    except Idea.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")

def tag_detail_view(request, pk):
    author = get_object_or_404(Author, id=pk)
    news_by_tag = author.news_set.all()
    return render(request, 'idea/news_by_tag.html', 
    {'news_by_tag': news_by_tag})

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect('add_idea')
            # редирект это куда отправит в случае удачного использования 
    else:
        form = AuthorForm()
    return render(request,'idea/create_author.html',{'form':form})