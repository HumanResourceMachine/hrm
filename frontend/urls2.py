from django.urls import path
import frontend.views2 as views
urlpatterns = [
    path('test2/', views.test),
    path('change_time/', views.change_time),
    path('view_time/', views.view_time),
    path('view_status/', views.view_status),
    path('view_applicants/', views.view_applicants),
]