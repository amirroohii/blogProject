from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView, Request, Response
from .serializers import SignUpSerializer
# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'User create successfully',
                'data': serializer.data,
                'status': status.HTTP_201_CREATED,
            }
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
