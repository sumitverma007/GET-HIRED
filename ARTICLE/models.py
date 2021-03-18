from django.db import models
from EMPLOYER.models import EMPLOYER
from JOBSEEKER.models import JOBSEEKER
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

    def __str__(self):
        return self.jobseeker + " likes "+article


class COMMENT(models.Model):
    jobseeker=models.ForeignKey(JOBSEEKER,on_delete=models.CASCADE)
    article=models.ForeignKey(ARTICLE,on_delete=models.CASCADE)
    commenttext=models.TextField(default="Nice insight")
    comments=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    timestamp=models.DateTimeField(default=now)

    

