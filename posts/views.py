from .serializer import PostSerializer
from .models import Post
from rest_framework import viewsets

# Create your views here.


class PostsViewSetView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
