from django.shortcuts import render,HttpResponse,redirect
from django.core.files.storage import FileSystemStorage
from .models import JOBSEEKER,QUALIFICATIONS
from EMPLOYER.models import EMPLOYER
from django.contrib.auth.models import User
from django.contrib import messages
from BASE.models import Follow
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
            emp_reg=EMPLOYER.objects.all()
            # print(emp_reg)
            logged_in_user=request.user.username
            emp_obj_follow=Follow.objects.filter(job_seeker=logged_in_user)
            emp_i_follow=[]
            for emp in emp_obj_follow:
                emp_i_follow.append(emp.employer)

            # print(emp_i_follow)
            emp_i_should_follow=[]
            for emp in emp_reg:
                if emp.user.username not in emp_i_follow:
                    emp_i_should_follow.append(emp)
                if(len(emp_i_should_follow)>10):
                    break;    
            
            user_qual=QUALIFICATIONS.objects.get(user=request.user)
            param={
                'jbasic':obj,
                'jqual':user_qual,
                'emp_i_should_follow':emp_i_should_follow,
            }
            
            return render(request,'JOBSEEKER/home.html/',param)
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