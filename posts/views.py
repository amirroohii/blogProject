from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from .serializer import PostSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class PostsView(APIView):
    serializer_class = PostSerializer
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
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Post added successfully',
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostRetrieveView(APIView):
    serializer_class = PostSerializer
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