from django.shortcuts import render, HttpResponse
import random
from posts.models import Post
from posts.forms import PostForm
 
def test_view(request):
    return HttpResponse(f'Hello world!{random.randint(1,100)}')

    
def home_page_view(request):
    return render(request, 'base.html')


def post_list_view(request):
    if request.method == "GET": 
        posts = Post.objects.all()
        return render (request, "posts/post_list.html", context = {"posts": posts})

def post_detail_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, "posts/post_detail.html", context={"post": post})

def post_create_view(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "posts/post_create.html", context={"form": form})
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_create.html", context={"form": form})
        elif form.is_valid():
            tags = form.cleaned_data.pop("tags")
            post = Post.objects.create(**form.cleaned_data)
            post.tags.set(tags)
            return render(request, "posts/post_detail.html", context={"post": post})
        