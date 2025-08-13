from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'phone', 'first_name','last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        phone = validated_data.pop('phone')
        first_name = validated_data.pop('first_name')
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=first_name
        )
        Profile.objects.create(user=user, phone=phone)
        return user


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)