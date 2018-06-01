from django.urls import path
import frontend.views1 as views

from django.http import JsonResponse
def testjson(request):
	return JsonResponse({
    "total": "2",
    "page": "1",
    "records": "2",
    "rows": [{
		"applicant_id":0,
		"job_id":1,
        "name": "akaisora",
        "status": 0,
        "interviewer": "park",
        "date": "2018-06-01"
	}]*15
	})

urlpatterns = [
    #path('test1/', views.test),
	path('view_applicants_list/', views.view_applicants_list),
	path('score_applicants/', views.score_applicants),
	path('edit_applicants_workflow/', views.edit_applicants_workflow),
	path('release_job/', views.release_job),
	#path('view_applicants_list/applicants_list',testjson),
	#path('users/release_job',testjson)
]