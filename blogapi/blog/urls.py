from django.urls import path
from .views import *

urlpatterns = [
    path('', ListCreateAPI.as_view(), name='list-create'),
    path('<int:pk>/', RUD.as_view(), name='cud'),
    path('users/', UsersList.as_view(), name='user-list'),
    path('user/<pk>/', UserDetail.as_view(), name='user-details')
]