from django.shortcuts import render, HttpResponse, redirect
import random
from posts.models import Post
from posts.forms import PostForm, PostForm2
from django.contrib.auth.decorators import login_required
 
def test_view(request):
    return HttpResponse(f'Hello world!{random.randint(1,100)}')

    
def home_page_view(request):
    return render(request, 'base.html')

@login_required(login_url="/login/")
def post_list_view(request):
    if request.method == "GET": 
        posts = Post.objects.all()
        return render (request, "posts/post_list.html", context = {"posts": posts})


@login_required(login_url="/login/")
def post_detail_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, "posts/post_detail.html", context={"post": post})


@login_required(login_url="/login/")
def post_create_view(request):
    if request.method == "GET":
        form = PostForm2()
        return render(request, "posts/post_create.html", context={"form": form})
    if request.method == "POST":
        form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_create.html", context={"form": form})
        elif form.is_valid():
            tags = form.cleaned_data.pop("tags")
            post = Post.objects.create(**form.cleaned_data)
            post.tags.set(tags)
            return redirect("/posts/")