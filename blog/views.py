from django.shortcuts import get_object_or_404, render

from blog.models import Post

def homepage(request):
    posts = Post.objects.all()

    post_ids = map(lambda post: post.pk, posts)
    post_titles = map(lambda post: post.title, posts)
    post_taglines = map(lambda post: post.tagline, posts)

    arguments = {"arguments": zip(post_ids, post_titles, post_taglines)}

    return render(request, "blog/homepage.html", arguments)

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    arguments = {
        "post_title": post.title,
        "post_tagline": post.tagline,
        "post_author": post.author.username,
        "post_date": post.date,
        "post_content": post.content,
    }
    
    return render(request, "blog/post.html", arguments)