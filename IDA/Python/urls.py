"""Python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve 
from Python.settings import MEDIA_ROOT, STATICFILES_DIRS

urlpatterns = [
    path('', lambda req: redirect('Home/')),
    path('admin/', admin.site.urls),
    path('Welcome/', include('Welcome.urls')),
    path('Home/', include('Home.urls')),
    path('Explore/', include('Explore.urls')),
    path('Contact/', include('Contact.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': STATICFILES_DIRS[0]}), 
]
