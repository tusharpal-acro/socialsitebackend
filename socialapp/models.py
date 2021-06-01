from django.db import models
from django.contrib.auth.models import User
 
class Post(models.Model):
    content = models.TextField()
    user=models.CharField(max_length=100)
    likes = models.IntegerField(default=0)

class PostLike(models.Model):
    post = models.ForeignKey(Post, related_name='postLikes',on_delete=models.CASCADE)
    like_user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return "Like" + "| [Post = " + (str)(self.post) + "]" + ", [like_user = " + self.like_user.username + "]"


class User_Detail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    country=models.CharField(max_length=100)
    signup_day=models.CharField(max_length=12)
    is_holiday=models.BooleanField()
    holiday_name=models.CharField(max_length=100)
    ip_address=models.CharField(max_length=15)
    latitude=models.CharField(max_length=15)
    longitude=models.CharField(max_length=15)