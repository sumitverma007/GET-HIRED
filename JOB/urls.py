from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('relevant-jobs/',views.relevant_jobs,name="relevant job"),
    path('job_application/',views.job_application,name="job application")
]
