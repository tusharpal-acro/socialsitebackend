from django.db.models import fields
from rest_framework import  serializers
from django.contrib.auth.models import User
from .models import Post,PostLike
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff','password']
        extra_kwargs = {'password': {'write_only': True}}
        

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('username','password')


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ('id','post','like_user')


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('user', 'id', 'likes', 'content',)