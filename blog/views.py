from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout as logout_user
from django.contrib.auth import login as login_user

from blog.models import Post, Comment

from blog.forms import CommentForm
from django.contrib.auth.forms import UserCreationForm

def homepage(request):
    posts = Post.objects.all()

    arguments = {
        "arguments": list(map(lambda post: (post.pk, post.title, post.tagline), posts)),
        "loggedin": request.user.is_authenticated,
    }

    return render(request, "blog/homepage.html", arguments)

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post__id=post_id)
    comments_arguments = list(map(lambda comment: (comment.user.username, comment.content), comments))

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            Comment.objects.create(user=request.user, post=post, content=comment_form.cleaned_data["content"])
            return redirect(f"/post/{post_id}")
    
    comment_form = CommentForm()

    arguments = {
            "post_title": post.title,
            "post_tagline": post.tagline,
            "post_author": post.author.username,
            "post_date": post.date,
            "post_content": post.content,
            "post_comments_arguments": comments_arguments,
            "post_comment_form": comment_form,
            "loggedin": request.user.is_authenticated,
    }

    return render(request, "blog/post.html", arguments)

def logout(request):
    logout_user(request)
    return redirect("/")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login_user(request, user)
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "blog/signup.html", {"form": form})