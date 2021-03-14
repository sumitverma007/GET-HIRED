from django.db import models
from EMPLOYER.models import EMPLOYER
from JOBSEEKER.models import JOBSEEKER
# Create your models here.

class JOB(models.Model):
    job_id=models.AutoField(primary_key=True)
    job_title=models.CharField(max_length=100)
    job_desc=models.TextField()
    pub_date=models.DateTimeField(auto_now=True)
    x_req=models.DecimalField(max_digits=5,decimal_places=2)
    xii_req=models.DecimalField(max_digits=5,decimal_places=2)
    grad_req=models.DecimalField(max_digits=5,decimal_places=2)
    employer_name=models.ForeignKey(EMPLOYER,on_delete=models.CASCADE)

    def __str__(self):
        return self.job_title+ ' by '+self.employer_name.name


class JOB_APPLICATIONS(models.Model):
    jobseeker_username=models.CharField(max_length=250)
    job_id=models.IntegerField()

    def __str__(self):
        return self.jobseeker_username     


class APPLICATIONS(models.Model):
    applicant=models.ForeignKey(JOBSEEKER,on_delete=models.CASCADE)
    applicant_job=models.ForeignKey(JOB,on_delete=models.CASCADE)            

class SHORTLISTED(models.Model):
    applicant=models.ForeignKey(JOBSEEKER,on_delete=models.CASCADE)
    message=models.TextField(null=True,blank=True)
    hasSeen=models.BooleanField(default=False)
    applicant_job=models.ForeignKey(JOB,on_delete=models.CASCADE)
