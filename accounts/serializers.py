from rest_framework import serializers
from .models import User
from rest_framework.validators import ValidationError

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email_exists = User.objects.filter(email__iexact=attrs['email']).exists()
        if email_exists:
            return ValidationError('you have already an account')

        return super().validate(attrs)
