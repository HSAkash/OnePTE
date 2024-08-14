"""rest freamwork import"""
from . import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics


class CreateUserView(generics.CreateAPIView):
    """create user"""
    serializer_class = serializers.UserSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.MyTokenObtainPairSerializer