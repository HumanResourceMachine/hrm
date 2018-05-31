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
    er_id= models.IntegerField(primary_key=True, db_column='FId')

class interviewee(models.Model):
    ee_id = models.IntegerField(primary_key=True, db_column='FId')

class hr(models.Model):
    hr_id= models.IntegerField(primary_key=True, db_column='FId')

class play(models.Model):
    play_id= models.IntegerField(primary_key=True, db_column='FId')
    user = models.ForeignKey(users,on_delete=models.CASCADE)
    er_id=models.ForeignKey(interviewer,on_delete=models.CASCADE)
    ee_id=models.ForeignKey(interviewee,on_delete=models.CASCADE)
    hr_id=models.ForeignKey(hr,on_delete=models.CASCADE)



class interview(models.Model):
    ee_id=models.ForeignKey(interviewee,on_delete=models.CASCADE)
    er_id=models.ForeignKey(interviewer,on_delete=models.CASCADE)
    date = models.DateTimeField(default = timezone.now)
    feedback= models.CharField(max_length=500,default='?')

class position(models.Model):
    position_id= models.IntegerField(primary_key=True, db_column='FId')
    job = models.CharField(max_length=50,default='?')
    location = models.CharField(max_length=50,default='?')
    excepted_salary= models.CharField(max_length=10,default='?')
    hr =models.ForeignKey(hr,on_delete=models.CASCADE)
    job_description = models.CharField(max_length=500,default='?')

class apply(models.Model):
    resume_path=models.CharField(max_length=500,default='?')
    status=models.IntegerField(max_length=10,default=0)
    date = models.DateTimeField(default = timezone.now)
    initial_salary =models.IntegerField(max_length=10,default=0)
    ee_id=models.ForeignKey(interviewee,on_delete=models.CASCADE)
    position_id=models.ForeignKey(position,on_delete=models.CASCADE)


