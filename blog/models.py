from django.db import models
from django import forms

# Create your models here.

class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content=models.TextField()
    short_desc=models.CharField(max_length=300,default="")
    slug=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now_add=True)

    

class Contact(models.Model):
   
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=10)
    desc=models.TextField(max_length=50)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Signup(models.Model):
   
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=50)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Photo(models.Model):

    Pic=models.ImageField(upload_to="imagefolder")      


class comment(models.Model):
    STATUS=(
        ('New','New'),
        ('True', 'True'),
        ('False','False')
    )
   
    
    
    name1 = models.CharField(max_length=70)
    
    subject=models.CharField(max_length=50,blank=True)
    comment1=models.CharField(max_length=250,blank=True)
    rate=models.IntegerField(default=1)
    ip=models.CharField(max_length=50)
    status=models.CharField(max_length=10,default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['subject','comment1','rate']