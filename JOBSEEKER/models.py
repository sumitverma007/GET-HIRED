from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class JOBSEEKER(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=255)
    dob=models.DateField()
    phone=models.IntegerField()

    def __str__(self):
        return self.first_name

class QUALIFICATIONS(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    x_marks=models.DecimalField(max_digits=5,decimal_places=2)
    xii_marks=models.DecimalField(max_digits=5,decimal_places=2)
    grad_marks=models.DecimalField(max_digits=5,decimal_places=2)
    profile_pic=models.ImageField(upload_to='JOBSEEKER/PROFILE/',blank=True)
    resume=models.FileField(upload_to='JOBSEEKER/RESUME/',blank=True)

    def __str__(self):
        return self.user.username       