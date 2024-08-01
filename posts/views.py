from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.request import Request
from .serializer import PostSerializer
from .models import Post, User
from rest_framework.response import Response
from rest_framework import status, generics, viewsets, mixins

# Create your views here.


class PostsView(APIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    model = Post

    def get(self, request: Request):
        queryset = self.model.objects.all()
        serializer = self.serializer_class(instance=queryset, many=True)
        response = {
            'message': 'There are Posts list',
            'data': serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)


    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['author'] = self.request.user
            serializer.save()
            response = {
                'message': 'Post added successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostRetrieveView(APIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    model = Post

    def get(self, request: Request, pk):
        instance = self.model.objects.get(id=pk)
        serializer = self.serializer_class(instance=instance)
        response = {
            'message': f'Post {pk}',
            'data': serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)

    def put(self, request: Request, pk):
        instance = self.model.objects.get(id=pk)
        data = request.data
        serializer = self.serializer_class(data=data, instance=instance)

        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Post updated successfully',
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serializer.errors)

    def delete(self, request: Request, pk):
        instance = self.model.objects.get(id=pk)
        instance.delete()
        response = {
            'message': 'Post deleted successfully',
        }
        return Response(data=response, status=status.HTTP_200_OK)

# class ListPostForAuthor(generics.GenericAPIView, mixins.ListModelMixin):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]
class ListPostForAuthorView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_post(self, author):
        return Post.objects.filter(author=author)

    def get(self, request: Request):
        posts = self.get_post(request.user)
        serializer = self.serializer_class(instance=posts, many=True)
        response = {
            'message': 'Author Posts',
            'posts': serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)

# @api_view(http_method_names=['GET'])
# def user_post_list(request: Request):
#     user = request.user
#     post = Post.objects.filter(author=user)
#     serializer = CurrentUserPostsSerializer(instance=post)
#     response = {
#         'message': 'Author posts',
#         'posts': serializer.data
#     }
#     return Response(data=response, status=status.HTTP_200_OK)


class PostsViewSetView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
