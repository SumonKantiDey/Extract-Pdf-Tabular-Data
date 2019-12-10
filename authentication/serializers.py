from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class UserSerilizers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserRegistrationSerilizers(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=True)
    # email = serializers.EmailField(
    #     validators=[UniqueValidator(queryset=User.objects.all())], required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=100, required=True)
    permissionview = serializers.CharField(max_length=100, required=True)

    def validate_email(self, email):
        is_already_exists = User.objects.filter(email=email).exists()
        if is_already_exists:
            raise serializers.ValidationError('already exists')
        return email

    def validate_username(self, username):
        is_already_exists = User.objects.filter(username=username).exists()
        if is_already_exists:
            raise serializers.ValidationError('already exists')
        return username

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'permissionview']
        # extra_kwargs = {'username': {'required': True},
        #                 'email': {'required': True}, 'password': {'required': True}}
