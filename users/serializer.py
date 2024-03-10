from rest_framework import serializers
from users.models import User


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        user_name = attrs.get('user_name')
        email=attrs.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Sorry, the email you entered is already taken.')
    
        if User.objects.filter(user_name=user_name).exists():
            raise serializers.ValidationError('Sorry, the username you entered is already taken.')
        return attrs
    
    
    def create(self, validated_data):
        user = User.objects.create_user(first_name='',**validated_data)
        return user