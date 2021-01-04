from django.db import models
from EMPLOYER.models import EMPLOYER
# Create your models here.
class ARTICLE(models.Model):
    article_id=models.AutoField(primary_key=True)
    tag=models.CharField(max_length=50)
    article_title=models.CharField(max_length=250)
    article_desc=models.TextField(blank=True)
    article_media=models.ImageField(upload_to='ARTICLE/MEDIA/',blank=True)
    employer_name=models.ForeignKey(EMPLOYER,on_delete=models.CASCADE)

    def __str__(self):
        return self.article_id+ ' by '+self.employer_name.name
