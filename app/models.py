from django.db import models

class JS(models.Model):
    name_js =models.CharField(max_length=50)
    email =models.EmailField(primary_key=True, default="test@gmail.com")
    mobile =models.IntegerField(default=9876543210)
    password =models.CharField(max_length=25)
    education =models.CharField(max_length=60)
    skills =models.CharField(max_length=60)
    location =models.CharField(max_length=60)
    resume =models.FileField(editable=True)
    profile = models.ImageField(editable=True)

class Company(models.Model):
    c_name =models.CharField(max_length=50)
    c_email = models.EmailField(primary_key=True,default="company@gmail.com")
    c_contact = models.IntegerField(default=9876543210)
    c_pw = models.CharField(max_length=50)
    c_address = models.TextField(max_length=100,default="Company Address")

class Jobs(models.Model):
    job_title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
    job_detail = models.TextField(max_length=1000)
    job_tags = models.TextField(max_length=1000)

class Admin(models.Model):
    ausr = models.CharField(max_length=20,primary_key=True)
    aemail = models.EmailField(default="admin@test.com")
    apw = models.CharField(max_length=20)

class Exams(models.Model):
    e_name = models.CharField(max_length=25)
    e_email = models.EmailField(default="test@gmail.com")
    e_mobile = models.IntegerField(default=9876543210)
    e_exams = models.TextField(max_length=50)

