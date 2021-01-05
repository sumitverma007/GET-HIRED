from django.shortcuts import render,HttpResponse,redirect
from .models import JOBSEEKER
# Create your views here.
def home(request):
    #check if user is anonymous
    
    if not request.user.is_authenticated:
        #send them to home
        return redirect('/')
        # return HttpResponse("USer not authenticated")
    #check if employer is trying to enter here by manually typing url
    else:
        try:
            obj=JOBSEEKER.objects.get(user=request.user)
            #if valid jobseeker
            #design JOBSSKER HOME PAGE
            
            return HttpResponse("VALID JOB SEEKER")
        #if not a valid user
        except:
            # return HttpResponse("NOT vALID  JS")
            return redirect('/')
                 
    # return HttpResponse("I am at end")