from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Post
from accounts.models import User


class PostSerializer(ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'author', 'title']


class AuthorPostDetailSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(view_name='post-detail', queryset=User.objects.all(), many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'posts']
