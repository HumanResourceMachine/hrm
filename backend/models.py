from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class users(models.Model):
    username = models.CharField(primary_key = True, max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=40)

    def __str__(self):
    # 在Python3中使用 def __str__(self):
        return self.username

class interviewer(models.Model):
    er_id= models.AutoField(primary_key=True)
    def __str__(self):
    # 在Python3中使用 def __str__(self):
        return str(self.er_id)

class interviewee(models.Model):
    ee_id = models.AutoField(primary_key=True)
    def __str__(self):
    # 在Python3中使用 def __str__(self):
        return str(self.ee_id)
class hr(models.Model):
    hr_id= models.AutoField(primary_key=True)
    def __str__(self):
    # 在Python3中使用 def __str__(self):
        return str(self.hr_id)

class play(models.Model):
    play_id= models.AutoField(primary_key=True)
    user = models.ForeignKey(users,on_delete=models.CASCADE)
    er_id=models.ForeignKey(interviewer,on_delete=models.CASCADE)
    ee_id=models.ForeignKey(interviewee,on_delete=models.CASCADE)
    hr_id=models.ForeignKey(hr,on_delete=models.CASCADE)


class position(models.Model):
    position_id= models.AutoField(primary_key=True)
    job = models.CharField(max_length=50,default='?')
    location = models.CharField(max_length=50,default='?')
    excepted_salary= models.CharField(max_length=10,default='?')
    hr =models.ForeignKey(hr,on_delete=models.CASCADE)
    job_description = models.CharField(max_length=500,default='?')
    def __str__(self):
    # 在Python3中使用 def __str__(self):
        return self.job
    def becomedict(self):
         ans={}
         ans["job"]=self.job
         ans["desc"]=self.job_description
         return ans



'''
0 提交完成
1 一面  -1 一面挂掉
2 二面   -2  二面挂掉
3 hr面   -3  hr面试挂掉
4 offer

'''
class apply(models.Model):
    apply_id= models.AutoField(primary_key=True)
    resume_path=models.CharField(max_length=500,default='?')
    status=models.IntegerField(default=0)
    date = models.DateTimeField(default = timezone.now)
    initial_salary =models.IntegerField(default=0)
    ee_id=models.ForeignKey(interviewee,on_delete=models.CASCADE)
    position_id=models.ForeignKey(position,on_delete=models.CASCADE)



class interview(models.Model):
    interview_id= models.AutoField(primary_key=True)
    ee_id=models.ForeignKey(interviewee,on_delete=models.CASCADE)
    er_id=models.ForeignKey(interviewer,on_delete=models.CASCADE)
    apply_id=models.ForeignKey(apply,on_delete=models.CASCADE)
    date = models.CharField(max_length=50,default='?')
    feedback= models.CharField(max_length=500,default='?')
    status=models.IntegerField(default=0)
