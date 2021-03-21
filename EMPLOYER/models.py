from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EMPLOYER(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.TextField()
    cin_num=models.IntegerField(unique=True,blank=False)
    email=models.EmailField(default="default@gmail.com")
    profile_pic=models.ImageField(upload_to='EMPLOYER/PROFILE',blank=True)

    def __str__(self):
        return self.name


