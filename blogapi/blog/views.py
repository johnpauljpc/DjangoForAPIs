from django.shortcuts import render
from .models import Post
from django.contrib.auth import get_user_model
from .serializers import PostSerializer, UserSerializer
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import (IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly,
                                         )
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class ListCreateAPI(ListCreateAPIView):
    # model = Post
    permission_classes = [IsAuthenticatedOrReadOnly ] #permission at view level, it ovverides that of the project level
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class RUD(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UsersList(ListCreateAPIView):
   
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer