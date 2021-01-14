from django.db import models

# Create your models here.

class Follow(models.Model):
    job_seeker=models.CharField(max_length=50)
    employer=models.CharField(max_length=50)

    def __str__(self):
        return self.job_seeker+" follows "+self.employer