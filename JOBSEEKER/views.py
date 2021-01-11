from django.shortcuts import render,HttpResponse,redirect
from django.core.files.storage import FileSystemStorage
from .models import JOBSEEKER,QUALIFICATIONS
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
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
            
            return render(request,'JOBSEEKER/home.html/')
        #if not a valid user
        except:
            # return HttpResponse("NOT vALID  JS")
            return redirect('/')
                 
    # return HttpResponse("I am at end")

def registerjobseeker(request):
    if request.method=='POST':
        username=request.POST.get('jUsername',None)
        password=request.POST.get('jPassword',None)
        first_name=request.POST.get('jFirstName',None)
        last_name=request.POST.get('jLastName',None)
        email=request.POST.get('jemail',None)
        x_marks=request.POST.get('jXmarks')
        xii_marks=request.POST.get('jXiimarks')
        grad_marks =request.POST.get('jGradmarks')
        dob=request.POST.get('jDob')
        phone=request.POST.get('jPhone')
        profile_pic=request.FILES.get('jProfilePic',None)
        resume=request.FILES.get('jResume',None)
        #try to create a user
        try:
            user=User.objects.create_user(username,email,password)
            try:
                jobseeker=JOBSEEKER(user=user,first_name=first_name,last_name=last_name,email=email,dob=dob,phone=phone)
                jobseeker.save()
                try:
                    qualification=QUALIFICATIONS(user=user,x_marks=x_marks,xii_marks=xii_marks,grad_marks=grad_marks,profile_pic=profile_pic,resume=resume)
                    qualification.save()
                    login(request,user)
                    return redirect("/")
                except:
                    jobseeker.delete()
                    messages.error(request,"Registration Failed:Please enter correct data")
                    return redirect('/handlesignup/')  
                

            except:
                user.delete()
                messages.error(request,"Registration Failed:Please enter correct data")    
                return redirect('/handlesignup/')  

        except:
          
            messages.error(request,"Registration Failed :Please enter correct data")
            return redirect('/handlesignup/')    
        

        return HttpResponse("Will register job seeker data")
    else:
        return redirect('/handlesignup/')        