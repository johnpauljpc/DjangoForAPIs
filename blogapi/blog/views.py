from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
class ListCreateAPI(ListCreateAPIView):
    # model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class RUD(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
