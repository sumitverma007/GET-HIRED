from django.shortcuts import render,HttpResponse,redirect
from .models import EMPLOYER
from ARTICLE.models import ARTICLE
from JOB.models import JOB
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




def publishpost(request):
    if request.method == 'POST':
        user=request.user
        #check if user is authenticated
        if user.is_authenticated:
            #valid user
            #check if it is employer
            try:
                employer=EMPLOYER.objects.get(user=user)
                article_tag=request.POST.get('article_tag')
                article_title=request.POST.get('article_title')
                article_desc=request.POST.get('article_desc')
                article_media=request.FILES.get('article_image')
                
                myarticle=ARTICLE(tag=article_tag,article_title=article_title,article_desc=article_desc,employer_name=employer,article_media=article_media)
                try:
                    myarticle.save()
                    messages.success(request,"Article published successfully")
                    return redirect('/')
                except:
                    messages.error(request,"Falied to publish.")
                    return redirect('/')    
                
                





                
            except:
                return redirect('/')    
        else:
            return redirect('/')    
    
   
    else:
        return redirect('/')    
    



def deletepost(request,id):
    #check if user is authenticated 
    if request.user.is_authenticated:
        # if employer
        try:
            employer=EMPLOYER.objects.get(user=request.user)
            #employer
            #get article
            try:
                article=ARTICLE.objects.get(article_id=id)
                if article.employer_name==employer:
                    article.delete()
                    messages.success(request,"Article deleted Successfully")
                else:
                    messages.error(request,"Permission Denied")

                return redirect('/')        
            
            except:
                messages.error(request,"No such article found")
        except:
            return redirect('/')    


    else:
        return redirect('/')    
        




def myjobs(request):
    # user is authenticated or not
    if request.user.is_authenticated:
        # a valid employer
        try:

            employer=EMPLOYER.objects.get(user=request.user)
            jobs=JOB.objects.filter(employer_name=employer)
            # print(jobs)
            param={
                'jobs':jobs
            }
            return render(request,'EMPLOYER/my-jobs.html/',param)


        except:
            return redirect('/')

    else:
        return redirect('/')    