from django.db import models
from django.contrib.auth.models import User

class PostRead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    text=models.TextField(max_length=100)
    read = models.ManyToManyField(User, related_name='reed_user', blank=True, through=PostRead)
    pubdate=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class UserFollowing(models.Model):
    user_id = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    