from django.db import models
from EMPLOYER.models import EMPLOYER
from JOBSEEKER.models import JOBSEEKER
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class ARTICLE(models.Model):
    article_id=models.AutoField(primary_key=True)
    tag=models.CharField(max_length=50)
    article_title=models.CharField(max_length=250)
    article_desc=models.TextField(blank=True)
    article_media=models.ImageField(upload_to='ARTICLE/MEDIA/',blank=True)
    employer_name=models.ForeignKey(EMPLOYER,on_delete=models.CASCADE)
    time_stamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "article  by "+self.employer_name.name


class LOVEDPOST(models.Model):
    jobseeker=models.ForeignKey(JOBSEEKER,on_delete=models.CASCADE)
    article=models.ForeignKey(ARTICLE,on_delete=models.CASCADE)

   
class COMMENT(models.Model):
    jobseeker=models.ForeignKey(JOBSEEKER,on_delete=models.CASCADE)
    article=models.ForeignKey(ARTICLE,on_delete=models.CASCADE)
    commenttext=models.TextField(default="Nice insight")
    comments=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    timestamp=models.DateTimeField(default=now)

    
class TOPIC(models.Model):
    topic_name=models.CharField(max_length=50)

    def __str__(self):
        return self.topic_name

class QUESTION(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    tag=models.ForeignKey(TOPIC,on_delete=models.CASCADE)
    title=models.CharField(max_length=500)
    desc=models.TextField()
    problem_link=models.URLField(max_length=200,null=True,blank=True)
    constraint=models.TextField(null=True,blank=True,default="default constraint")
    p_in=models.TextField(null=True,blank=True)
    p_out=models.TextField(null=True,blank=True)
    p_exin=models.TextField(null=True,blank=True)
    p_exout=models.TextField(null=True,blank=True)
    p_code=models.TextField(null=True,blank=True)
    pyurl=models.URLField(max_length=200,null=True,blank=True,default="https://www.google.com/")

    