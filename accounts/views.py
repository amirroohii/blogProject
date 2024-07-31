from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView, Request, Response
from .serializers import SignUpSerializer
from django.contrib.auth import authenticate
from .tokens import create_jwt_pair_for_user
# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'User create successfully',
                'data': serializer.data,
            }
            return Response(response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = []

    def post(self, request: Request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)

            response = {
                'message': 'login successfully',
                'token': tokens
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request):
        content = {
            'auth': str(request.auth),
            'user': str(request.user),
        }

        return Response(data=content, status=status.HTTP_200_OK)