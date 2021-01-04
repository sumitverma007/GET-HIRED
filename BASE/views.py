from django.shortcuts import render,HttpResponse,redirect
from JOBSEEKER.models import JOBSEEKER
from EMPLOYER.models import EMPLOYER

def indexhome(request):
    # return HttpResponse("Ok initial set up ok")
    #The very function which will be invoked
    return render(request,'BASE/login.html/')

def handleuser(request):
    #if user is already logged in then send them to their respective views 
    if request.user.is_authenticated:
        
        try:
            user=JOBSEEKER.objects.get(user=request.user)
            return redirect('/JOBSEEKER/home/')
            
        except:
            return redirect('/EMPLOYER/home/')
            
    #The user is not authenticated or somehow entered the wrong url as anonynmous
    else:
        return render(request,'BASE/login.html/')        
    
       


