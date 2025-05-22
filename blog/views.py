from django.shortcuts import get_object_or_404, render

from blog.models import Post, Comment

def homepage(request):
    posts = Post.objects.all()

    arguments = {"arguments": map(lambda post: (post.pk, post.title, post.tagline), posts)}

    return render(request, "blog/homepage.html", arguments)

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post__id=post_id)
    comments_arguments = map(lambda comment: (comment.user.username, comment.content), comments)
    arguments = {
        "post_title": post.title,
        "post_tagline": post.tagline,
        "post_author": post.author.username,
        "post_date": post.date,
        "post_content": post.content,
        "post_comments_arguments": comments_arguments,
    }
    
    return render(request, "blog/post.html", arguments)