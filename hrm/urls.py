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
    url(r'^users/$',backend_views.user),
    url(r'^users/login/$',backend_views.login),
    url(r'^users/logout/$',backend_views.logout),
    url(r'^interview/time/$',backend_views.interview_time),
    url(r'^interview/status/$',backend_views.get_interview_status),
    url(r'^interview/resume/$',backend_views.get_resume_path),




    url(r'^release_job/$',backend_views.release_job),
    url(r'^apply_job/$',backend_views.apply_job),
    url(r'^upload_resume/$',backend_views.upload_resume),
    url(r'^resume/$',backend_views.upload_resume),
    url(r'^arrangement_interview/$',backend_views.arrangement_interview),
    url(r'^feedback/$',backend_views.feedback),





]\
+ frontend.urls1.urlpatterns\
+ frontend.urls2.urlpatterns\
+ frontend.urls3.urlpatterns\
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
