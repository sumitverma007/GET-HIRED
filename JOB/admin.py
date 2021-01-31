from django.contrib import admin
from .models import JOB,JOB_APPLICATIONS,APPLICATIONS,SHORTLISTED
# Register your models here.
admin.site.register(JOB)
admin.site.register(JOB_APPLICATIONS)
admin.site.register(APPLICATIONS)
admin.site.register(SHORTLISTED)
