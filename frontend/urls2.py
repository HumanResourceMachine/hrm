from django.urls import path
import frontend.views2 as views
urlpatterns = [
    path('test2/', views.test),
    path('change_time/', views.change_time),
    path('view_time/', views.view_time),
    path('view_status/', views.view_status),
    path('view_applicants/', views.view_applicants),
    path('test/interview/time', views.interview_time),
    path('test/interview/status', views.interview_status),
    path('test/users', views.users),
]