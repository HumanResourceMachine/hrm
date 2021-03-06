from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from backend.models import users,interviewer,interviewee,hr,play,interview,position,apply
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from datetime import datetime
import  time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from PIL import Image
from email.utils import formataddr
import urllib.request
import random
import  os

@csrf_exempt
#新建用户 get用户信息
def user(request):
    result = {'verdict': 'ok', 'message': 'successful!'}
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        username = str(username)
        password = str(password)
        email = str(email)
        result['email'] = email
        result['password'] = password
        result['username'] = username
        #return JsonResponse(result)
        userinfo = users.objects.filter(Q(email = email)|Q(username = username))
        print (userinfo)
        if userinfo:
            result['verdict'] = 'error'
            result['message'] = 'The email or username already exits!'
        else:
            user = users(username = username , password = password ,email = email)

            iner = interviewer.objects.create()
            inee =interviewee.objects.create()
            ihr =hr.objects.create()
            user.save()
            print(iner.er_id)
            play.objects.create(user=user,er_id=iner,ee_id=inee,hr_id=ihr)

        return JsonResponse(result)
    else :
        username = request.session.get('username','')
        userinfo = users.objects.filter(username=username)
        if userinfo:
            result['username'] = username
            result['email'] = str(list(userinfo.values('email'))[0]['email'])
            result['role'] = str(request.session["role"])
            #result['avatar'] = '/media/'+str(list(userinfo.values('avatar'))[0]['avatar'])
        else:
            result['verdict'] = 'error'
            result['message'] = 'Please log in first!'
        return JsonResponse(result)

#登录
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        role=int(role)
        result = {'verdict': 'ok', 'message': 'successful'}
        userinfo = users.objects.filter(username = username,password = password)
        if userinfo:
            request.session["username"] = username
            print("FUCK!!!!!!!!!!!!!!!!!!!!!!")
            print (request.session["username"])
            if role==0:
                request.session["role"] = 0
            elif role ==1:
                request.session["role"] = 1
            elif role == 2:
                request.session["role"] = 2
            else:
              result['verdict'] = 'error'
              result['message'] = 'Please select your role!'
        else:
            print ("login error!")
            result['verdict'] = 'error'
            result['message'] = 'The Username or Password is not correct.'
        return JsonResponse(result)

#登出
def logout(request):
    del request.session["username"]
    result = {'verdict':'ok','message':'successful'}
    return render(request, "login.html")



'''
POST 确定面试时间
参数
ee_id
time
er_id
pos_id
返回
verdict
message

ee_id pos_id ->apply_id
er_id  time ee_id apply_id  => interview

GET 得到面试时间

返回
interviews:

[  {    "job_title": "Google SDE",    "date":  [y,mo,d] },
  {    "job_title": "Amazon SDE",    "date":  [y,mo,d] ]

user  -> apply->interview

'''


@csrf_exempt
def interview_time(request):
    result = {'verdict': 'ok', 'message': 'successful!'}
    if request.method == 'POST':
        time = request.POST['time']
        interviewer_id=request.POST['er_id']
        interviewee_id=request.POST['ee_id']
        position_id = request.POST['pos_id']
        interviewee_id=int(interviewee_id)
        interviewer_id=int(interviewer_id)
        position_id=int(position_id)

        iinterviewer=interviewer.objects.get(er_id=interviewer_id)
        iinterviewee=interviewee.objects.get(ee_id=interviewee_id)
        iposition=position.objects.get(position_id=position_id)
        iapply=apply.objects.get(ee_id=iinterviewee,position_id=iposition)

        interview.objects.create(er_id=iinterviewer,ee_id =iinterviewee,apply_id=iapply,date=time)
        return JsonResponse(result)

    if request.method == 'GET':
        interviews=[]
        username = request.session.get('username','')
        userinfo = users.objects.get(username=username)
        iplay =play.objects.get(user=userinfo)
        print (iplay.user.username)
        iapply=apply.objects.filter(ee_id=iplay.ee_id)
        for iiapply in iapply:
            iinterview=interview.objects.filter(apply_id=iiapply)
            for iiinterview in iinterview:
                ainterview={}
                ainterview["job_title"]=iiinterview.apply_id.position_id.job
                ainterview["date"]=iiinterview.date
                interviews.append(ainterview)
        result['interviews']=interviews
        return JsonResponse(result)



@csrf_exempt
#发布岗位
def release_job(request):
    result = {'verdict':'ok','message':'successful'}
    if request.method == 'POST':
        job = request.POST['job']
        job_description = request.POST['job_description']
        excepted_salary = request.POST['excepted_salary']
        location=request.POST['location']

        result['job'] = job
        result['job_description'] = job_description
        result['excepted_salary'] = excepted_salary
        result['location'] = location

        username = request.session.get('username','')
        userinfo = users.objects.get(username=username)
        if userinfo:
            print( userinfo.email)
            iplay=play.objects.get(user=userinfo)
            print (iplay.hr_id)
            position.objects.create(job=job,location=location,excepted_salary=excepted_salary,
            job_description=job_description,hr=iplay.hr_id)
        else:
            result['verdict'] = 'fail'
            result['message'] = "The hr don't exits!"
        return JsonResponse(result)




# 返回面试状态
def get_interview_status(request):
    result = {'verdict':'ok','message':'successful'}
    if request.method == 'GET':
        interviews=[]
        username = request.session.get('username','')
        userinfo = users.objects.get(username=username)
        iplay =play.objects.get(user=userinfo)
        print (iplay.user.username)
        iapply=apply.objects.filter(ee_id=iplay.ee_id)
        for iiapply in iapply:
            iinterview=interview.objects.filter(apply_id=iiapply)
            for iiinterview in iinterview:
                ainterview={}
                ainterview["job_title"]=iiinterview.apply_id.position_id.job
                ainterview["status"]=iiinterview.status
                interviews.append(ainterview)
        result['interviews']=interviews
        return JsonResponse(result)




@csrf_exempt
# 申请工作
def apply_job(request):
    if request.method == "POST":
        username = request.session.get('username','')
        pos_id = request.POST['pos_id']
        print (username)
        result = {'verdict':'error','message':'No resume!'}
        resume =request.FILES.get("resume", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not resume:
            return JsonResponse(result)

        userinfo = users.objects.get(username=username)


        if userinfo:
            x= str(random.randint(1, 20000000))
            resume_path=os.path.join("media", username+x+resume.name)

            iplay=play.objects.get(user=userinfo)
            ipos=position.objects.get(position_id=int(pos_id))
            apply.objects.create(resume_path=resume_path,ee_id=iplay.ee_id,position_id=ipos)


        destination = open(resume_path,'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in resume.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()

        return render(request, "apply_job.html")


@csrf_exempt
# 得到简历的路径
def get_resume_url(request):
    result = {'verdict':'ok','message':'successful'}
    if request.method == "POST":
        iinterviewee = request.POST['ee_id']
        iposition = request.POST['pos_id']
        interviewee_obj=interviewee.objects.get(ee_id=iinterviewee)
        position_obj=position.objects.get(position_id=iposition)
        iapply=apply.objects.get(ee_id=interviewee_obj,position_id=position_obj)
        result["resume_url"]=iapply.resume_path
       # print (result["resume_url"])
        return JsonResponse(result)




# 得到工作信息
def get_job_information(request):
    result = {'verdict':'ok','message':'successful'}
    job_list=[]
    if request.method == "GET":
        positions=position.objects.all()
        for i in positions:
          job_list.append(i.becomedict())
        result["job_list"]=job_list
        return JsonResponse(result)




@csrf_exempt
# 所有申请者情况信息
def applicants_list(request):
    result = {'verdict':'ok','message':'successful'}
    if request.method == 'POST':
        result["page"]="1"
        jishuqi=0
        rows=[]
        jishuqi=apply.objects.all().count()
        applys=apply.objects.all()
        for app in applys:
            row={}
            row["applicant_id"]=app.ee_id.ee_id
            row["job_id"]=app.position_id.position_id
            iplay=play.objects.get(ee_id=app.ee_id)
            row["interviewer"]=iplay.user.username  #面试者名字
            row["status"]=app.status

            iinterview=interview.objects.get(apply_id=app)
            iplay=play.objects.get(er_id=iinterview.er_id)
            row["name"]=iplay.user.username            #面试官名字
            iinterview=interview.objects.get(apply_id=app)
            row["date"]=iinterview.date  #面试时间
            rows.append(row)


        result["total"]=jishuqi
        result["records"]=jishuqi
        result["rows"]=rows
        return JsonResponse(result)





