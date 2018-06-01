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


@csrf_protect
#新建用户 get用户信息
def user(request):
    result = {'verdict': 'ok', 'message': 'successful!'}
    if request.method == 'POST':
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
        if userinfo:
            result['verdict'] = 'error'
            result['message'] = 'The email or username already exits!'
        else:
            user = users(username = username , password = password ,email = email ,friendnum = 0)
            user.save()
            interviewer = interviewer()
            interviewer.save()
            interviewee =interviewee()
            interviewee.save()
            hr = hr()
            hr.save()
            play=play(user=user,er_id=interviewer,ee_id=interviewee,hr_id=hr)
        return JsonResponse(result)
    else :
        username = request.session.get('username','')
        userinfo = users.objects.filter(username=username)
        if userinfo:
            result['username'] = username
            result['email'] = str(list(userinfo.values('email'))[0]['email'])
            result['role'] = request.session["role"]
            #result['avatar'] = '/media/'+str(list(userinfo.values('avatar'))[0]['avatar'])
        else:
            result['verdict'] = 'error'
            result['message'] = 'Please log in first!'
        return JsonResponse(result)

#登录
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    role = request.POST['role']
    username = str(username)
    password = str(password)
    result = {'verdict': 'ok', 'message': 'successful'}
    userinfo = users.objects.filter(username = username,password = password)
    if userinfo:
        request.session["username"] = username
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
        result['verdict'] = 'error'
        result['message'] = 'The Username or Password is not correct.'
    return JsonResponse(result)

#登出
def logout(request):
    del request.session["username"]
    result = {'verdict':'ok','message':'successful'}
    return JsonResponse(result)

def interview_time(request):
     result = {'verdict': 'ok', 'message': 'successful!'}
    if request.method == 'POST':
        interviewee_id = request.POST['ee_id']
        time = request.POST['time']
        interviewer_id=request.POST['er_id']
        position_id = request.POST['pos_id']
        interviewee_id=int(interviewee_id)
        interviewer_id=int(interviewer_id)
        position_id=int(position_id)
        apply =apply.objects.filter(ee_id =interviewee_id,position_id=position_id)
        interviewinfo = interview.objects.filter(er_id=interviewer_id,ee_id =interviewee_id,status=apply.status)
        if interviewinfo:
          //下面这一行有bug
            interviewinfo.date=time
        else:
           result['verdict'] = 'error'
           result['message'] = 'This is not correct.'
        return JsonResponse(result)
   if request.method == 'GET':
      interviews=[]
      interviewee_id = request.POST['ee_id']
      interviewee_id=int(interviewee_id)
      applys =apply.objects.filter(ee_id =interviewee_id)
      for apply in applys:
        interviewinfo = interview.objects.filter(ee_id =interviewee_id,status=apply.status,er_id=apply.interviewer_id,)
        interview["job_title"]=
        interview["start"]=
        interview["end"]=
        interviews.append()














#发布岗位
def release_job(request):
    result = {'verdict':'ok','message':'successful'}
    if request.method == 'POST':
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
        if userinfo:
            result['verdict'] = 'fail'
            result['message'] = 'The email or username already exits!'
        else:
            users.objects.create(username = username , password = password ,email = email ,friendnum = 0)
        return JsonResponse(result)

# 上传简历
def upload(request):
    if request.method == "POST":
        inp_file = request.FILES          # 上传的文件会在request.FILES里
        file_obj1 = inp_file.get('f1')    # 根据前端设置的name属性值获取相对应的文件

        print inp_file
        print file_obj1.name              # 获取文件名
        print file_obj1.size
        f = open(file_obj1.name, 'wb')    # 以获取的文件名 按‘wb’的方式打开一个文件
        for line in file_obj1.chunks():   # chunks方法读取文件，默认每次读取64kb
            f.write(line)
        f.close()
    return render(request, 'home/upload.html')


# 返回面试状态
def get_interview_status(request):
    if request.method == "GET":







