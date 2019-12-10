from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import UserSerilizers, UserRegistrationSerilizers
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
from django.contrib.auth.models import Group
from rest_framework import status
# Create your views here.


class RegistrationView(viewsets.ModelViewSet):
    serializer_class = UserSerilizers

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserRegistrationSerilizers
        return UserSerilizers

    def get_queryset(self):
        queryset = User.objects.filter(is_active=True)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = UserRegistrationSerilizers(data=request.data)
        if serializer.is_valid():
            user = User.objects.create(
                username=serializer.data.get('username'),
                email=serializer.data.get('email'),
            )
            user.set_password(serializer.data.get('password'))
            my_group = Group.objects.get(
                name=serializer.data.get('permissionview'))
            user.save()
            my_group.user_set.add(user)
            return Response({'message': 'Successfully user created'})

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class Authenticate_user(viewsets.ModelViewSet):
    serializer_class = UserSerilizers
    #permission_classes = [IsAdminUser, ]
    #g1 = Group.objects.create(name='BrokerView')
    # g1.save()
    serializer_class = UserSerilizers

    def get_queryset(self):
        queryset = User.objects.filter(is_active=True)
        cnt = 0
        for names in queryset:
            cnt += 1
            print(names)
            if cnt <= 2:
                my_group = Group.objects.get(name='BrokerView')
                my_group.user_set.add(names)
        return queryset
