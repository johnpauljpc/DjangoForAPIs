
from django.contrib import admin
# import rest_framework
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

from drf_yasg.views import get_schema_view as gsv
from drf_yasg import openapi
from rest_framework import permissions


schema_view = gsv( # new
openapi.Info(
title="Blog API",
default_version="v1",
description="A sample API for learning DRF",
terms_of_service="https://www.google.com/policies/terms/",
contact=openapi.Contact(email="contact@blogapi.com"),
license=openapi.License(name="BSD License"),
),
public=True,
permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('blog.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('allauth/', include('allauth.urls')),
    path('rest-auth/register/', include('dj_rest_auth.registration.urls')),
    path('openapi', get_schema_view(
        title="Blog API",
        description="Documentation of Blogapi endpoints",
        version="1.0.0"
    ), name="openapi-schema"),
    #Swagger UI API documentation link
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),

    #REDOC
    path('re-doc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),

    # Endpoints as a result of drf_yasg
    path('swagger/', schema_view.with_ui( # new
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]
