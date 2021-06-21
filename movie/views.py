from django.shortcuts import get_list_or_404, render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import render, get_object_or_404, redirect
import re

def movie_list(request):
    return render(request, 'movie/movie_list.html')

def post_detail(request, pk):
    print(pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'movie/post_detail.html', {'post': post})

def post_new(request, title):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.movie_title = title
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return redirect('post_list', title=post.movie_title)
    else:
        form = PostForm()
        return render(request, 'movie/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list', title=post.movie_title)
    else:
        form = PostForm(instance=post)
        return render(request, 'movie/post_edit.html', {'form': form})

def post_list(request, title):
    posts = Post.objects.filter(movie_title=title)
    return render(request, 'movie/post_list.html', {'posts': posts, 'title': title})