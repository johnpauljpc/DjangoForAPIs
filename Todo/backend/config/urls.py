
from django.contrib import admin
from django.urls import path, include
from todos.views import testV

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', include('todos.urls')), 
]
