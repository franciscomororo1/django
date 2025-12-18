from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from blog.forms import PostForm
from .models import Post
from django.utils import timezone

def post_list(request):
    post=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'post_list':post})

def post_detail(request, pk):
    post= get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {'post' :post})

@login_required
def post_new(request):
    if request.method =="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Altere para a página inicial
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
