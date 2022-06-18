from gc import get_objects
from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm, CommentForm

def post_list(request):
    # qs = Post.objects.filter(status='published') # here i dont want drafts to be seen on FE
    qs = Post.objects.all()
    context = {
        "object_list": qs
    }
    return render(request, "app/post_list.html", context)

def post_create(request):
    # form = PostForm(request.POST or None, request.FILES or None)
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("app:list")
    context = {
        'form':form
    }
    return render(request, 'app/post_create.html', context)


def post_detail(request, slug): # used pk instead of slug
    # print(request.path)
    # obj = get_objects(Post, slug=slug)
    # obj = Post.objects.get(slug=slug)
    # obj = Post.objects.get(pk=pk)
    form = CommentForm()
    obj = Post.objects.get(slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('app:detail', slug=slug)
            # return redirect(request.path) # redirect to the same page
    context = {
        "object":obj,
        "form": form,
    }
    return render(request, "app/post_detail.html", context)

def post_update(request, slug):
    # obj = get_objects(Post, slug=slug)
    # obj = Post.objects.get(pk=pk)
    obj = Post.objects.get(slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("app:list")

    context = {
        "object": obj,
        "form": form
    }
    return render(request, "app/post_update.html", context)

def post_delete(request, slug):
    obj = Post.objects.get(slug=slug)
    # obj = Post.objects.get(pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("app:list")
    context = {
        "object": obj
    }
    return render(request, "app/post_delete.html", context)

