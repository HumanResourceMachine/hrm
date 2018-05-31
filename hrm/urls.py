"""hrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
import frontend.views1, frontend.views2, frontend.views3, backend.views
import frontend.urls1, frontend.urls2, frontend.urls3
from django.conf.urls.static import static
from backend import views as backend_views
from django.contrib import admin
from django.conf.urls import include, url






urlpatterns = [

]\
+ frontend.urls1.urlpatterns\
+ frontend.urls2.urlpatterns\
+ frontend.urls3.urlpatterns\
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
