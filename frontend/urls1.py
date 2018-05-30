from django.urls import path
import frontend.views1 as views
urlpatterns = [
    path('test1/', views.test),
]