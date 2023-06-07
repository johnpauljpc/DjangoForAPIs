from django.urls import path
from .views import *

urlpatterns = [
    path('', ListCreateAPI.as_view(), name='list-create'),
    path('<pk>/', RUD.as_view(), name='cud')
]