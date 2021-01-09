from django.shortcuts import render,HttpResponse,redirect
from JOBSEEKER.models import JOBSEEKER
from EMPLOYER.models import EMPLOYER
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
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
    
       
def handlelogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        data={}
        if user is not None:
            login(request,user)
            data={
                'is_ok':1
            }
        else:
            data={
                'is_ok':0
            }    
        
        return JsonResponse(data)

    else:
        return redirect('/')    


def handlesignup(request):
    # return HttpResponse("Signup Here")
    return render(request,'BASE/signup.html')
    

def validateusername(request):
    # print(request.method) 
    username=request.GET.get('username',None)
    if username is None:
        return redirect("/")
    else:
        data={}
        p1=User.objects.filter(username__iexact=username).exists()
        # print(p1)
        data={
            'is_ok':p1
        }
        return JsonResponse(data)

          
    
