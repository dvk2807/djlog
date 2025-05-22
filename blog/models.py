from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=512, default="Unnamed post")
    tagline = models.CharField(max_length=1024, default="No tagline was provided to this post.")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date = models.DateField()
    content = models.TextField(max_length=65536, default="<p>No content was provided for this post.</p>")

    def __str__(self):
        return f"Post #{self.pk} '{self.title}' by User{self.author.username} on {self.date}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(max_length=8192, blank=False)

    def __str__(self):
        return f"Comment #{self.pk} by User {self.user.username} on Post #{self.post.pk}"