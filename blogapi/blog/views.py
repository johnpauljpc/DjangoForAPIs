from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

# Create your views here.
class ListCreateAPI(ListCreateAPIView):
    # model = Post
    permission_classes = [IsAuthenticatedOrReadOnly ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class RUD(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
