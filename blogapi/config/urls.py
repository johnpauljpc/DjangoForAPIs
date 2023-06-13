
from django.contrib import admin
# import rest_framework
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('blog.urls')),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('allauth/', include('allauth.urls')),
    path('rest-auth/register/', include('dj_rest_auth.registration.urls'))
]
