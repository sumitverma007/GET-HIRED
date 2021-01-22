from django.shortcuts import render,HttpResponse,redirect
from .models import EMPLOYER
from ARTICLE.models import ARTICLE
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
# Create your views here.
def home(request):
    # print(request.user)
    #check if user is authenticated
    if not request.user.is_authenticated:
        return redirect('/')
    #user is logged in
    else:
        #check if  a valid employer
        try:
            user=EMPLOYER.objects.get(user=request.user)
            # print("Valid Employer")
            try:

                posts=ARTICLE.objects.filter(employer_name=user).order_by('-article_id')
                # print(posts)
                param={
                    'posts':posts,
                }
                return render(request,'EMPLOYER/home.html/',param)
            except:    
                return render(request,'EMPLOYER/home.html/')
        except:
            print("Not a valid Employer")
            return redirect('/')    


def registeremployer(request):
    if request.method=='POST':
        username=request.POST.get('eUsername')
        password=request.POST.get('ePassword')
        email=request.POST.get('eEmail')
        cin_no=request.POST.get('eCin')
        name=request.POST.get('eName')
        profile_pic=request.FILES.get('eProfilepic')
        
        # return HttpResponse("Valid Employer")
        try:
            user=User.objects.create_user(username,email,password)
            try:
                employer=EMPLOYER(user=user,name=name,cin_num=cin_no,profile_pic=profile_pic)
                employer.save()
                login(request,user)
                return redirect('/')
            except:
                user.delete()
                messages.error(request,"Registration Failed ! Please Enter Correct data")
                return redirect("/handlesignup/")    
        except:
            messages.error(request,"Registration Failed ! Please Enter Correct data")
            return redirect('/handlesignup/')    
        
        
    else:
        return redirect('/handlesignup/')    
