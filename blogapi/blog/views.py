from django.shortcuts import render
from .models import Post
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly, IsUserOrReadOnly

# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly ] #permission at view level, it ovverides that of the project level
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UsersViewset(viewsets.ModelViewSet):
    permission_classes = ( IsUserOrReadOnly, )
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


