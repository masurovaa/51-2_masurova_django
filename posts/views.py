from django.shortcuts import render, HttpResponse, redirect
import random
from posts.models import Post
from posts.forms import PostForm, PostForm2, SearchForm
from django.contrib.auth.decorators import login_required


limit = 3
page = 3

start = (page - 1) * limit
end = page * limit


 
def test_view(request):
    return HttpResponse(f'Hello world!{random.randint(1,100)}')

    
def home_page_view(request):
    return render(request, 'base.html')

@login_required(login_url="/login/")
def post_list_view(request):
    limit = 3
    if request.method == "GET": 
        posts = Post.objects.all()
        form = SearchForm()
        search_q = request.GET.get("search_q")
        category_id = request.GET.get("category_id")
        ordering = request.GET.get("ordering")
        page = int(request.GET.get("page", 1))
        if category_id:
            posts = posts.filter(category_id=category_id)
        if search_q:
            posts = posts.filter(title__icontains=search_q)
        if ordering:
            posts = posts.order_by(ordering)

        max_pages = posts.count() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) +1
        elif round(max_pages) == max_pages:
           max_pages = round(max_pages)
        start = (page-1) * limit
        end = page * limit

        return render (request, "posts/post_list.html", context = {"posts": posts, "form": form, "max_pages": range(1, int(max_pages) + 1),},)


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