from django.shortcuts import render,HttpResponse,redirect
from django.core.files.storage import FileSystemStorage
from JOBSEEKER.models import JOBSEEKER,QUALIFICATIONS
from EMPLOYER.models import EMPLOYER
from django.contrib.auth.models import User
from django.contrib import messages
from BASE.models import Follow
from .models import ARTICLE,LOVEDPOST,COMMENT,TOPIC,QUESTION
from JOB.models import SHORTLISTED,APPLICATIONS
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
import random

# Create your views here.

def prepare(request):
    if request.user.is_authenticated:
        try:
            jobseeker=JOBSEEKER.objects.get(user=request.user)
            notifications=SHORTLISTED.objects.filter(applicant=jobseeker,hasSeen=False)
            topics=TOPIC.objects.all()
            notlen=len(notifications)
            param={
                'notlen':notlen,
                'tags':topics,
            }
            return render(request,"JOBSEEKER/preparation.html/",param)


        except:
            return redirect('/')    

    else:
        return redirect('/')    


def showproblem(request,tagname):
    tag=TOPIC.objects.get(topic_name=tagname)
    problems=QUESTION.objects.filter(tag=tag)
    param={
        'problems':problems,
        'tag':tag,
    }
    return render(request,'JOBSEEKER/problems.html/',param)


def problemdetail(request,tagname,id):
    problem=QUESTION.objects.get(id=id)
    param={
        'problem':problem,
    } 
    return render(request,'JOBSEEKER/problemdetail.html/',param)