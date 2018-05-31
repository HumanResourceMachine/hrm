from django.urls import path
import frontend.views1 as views
urlpatterns = [
    #path('test1/', views.test),
	path('view_applicants_list/', views.view_applicants_list),
	path('score_applicants/', views.score_applicants),
	path('edit_applicants_workflow/', views.edit_applicants_workflow),
	path('release_job/', views.release_job),
]