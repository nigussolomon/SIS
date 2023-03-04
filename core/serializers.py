from django.forms import PasswordInput
from rest_framework import serializers
from .models import SisUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class SisUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SisUser
        fields = ["id", "email", "first_name", "last_name", "user_type"]


class CreateSisUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=SisUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password], style={'input_type': 'password', 'placeholder': 'Password'}
    )
    password_confirmation = serializers.CharField(write_only=True, required=True,style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = SisUser
        fields = ("email", "first_name", "last_name", "password", "password_confirmation", "user_type")

    def validate(self, attrs):
        if attrs["password"] != attrs["password_confirmation"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        user = SisUser.objects.create_user(
            email=validated_data["email"],
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
            user_type = validated_data["user_type"],
            password = validated_data["password"]
        )
        user.save()
        return user
