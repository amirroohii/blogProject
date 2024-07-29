from rest_framework import serializers
from .models import User

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
