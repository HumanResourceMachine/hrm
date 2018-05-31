from django.urls import path
import frontend.views3 as views
urlpatterns = [
    path('test3/', views.test),
    path('login/', views.login),
    path('register/', views.register),
    path('apply_job', views.apply_job),
    path('view_job_info', views.view_job_info),
]