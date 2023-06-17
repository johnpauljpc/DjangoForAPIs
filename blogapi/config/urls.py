
from django.contrib import admin
# import rest_framework
from django.urls import path, include
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('blog.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('allauth/', include('allauth.urls')),
    path('rest-auth/register/', include('dj_rest_auth.registration.urls')),
    path('openapi', get_schema_view(
        title="Blog API",
        description="A sample API for learning DRF",
        version="1.0.0"
    ), name="openapi-schema"),
]
