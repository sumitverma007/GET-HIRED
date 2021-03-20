from django.shortcuts import render,HttpResponse,redirect
from django.core.files.storage import FileSystemStorage
from .models import JOBSEEKER,QUALIFICATIONS
from EMPLOYER.models import EMPLOYER
from django.contrib.auth.models import User
from django.contrib import messages
from BASE.models import Follow
from ARTICLE.models import ARTICLE,LOVEDPOST,COMMENT 
from JOB.models import SHORTLISTED
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
import random
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
            #get the recent posts of employer job seeker follow
            recent_posts=[]
            for emp in emp_i_follow:
                try:
                    p_emp=User.objects.get(username=emp)
                    req_employer=EMPLOYER.objects.get(user=p_emp)
                    article_by_them=ARTICLE.objects.filter(employer_name=req_employer).order_by('-article_id')[0:3]
                    recent_posts.extend(article_by_them)
                    



                except Exception as e:
                    print("Except part")
                    print(e)     
            random.shuffle(recent_posts)   
              
            target_post=[]

            for post in recent_posts:
                lovedpost=LOVEDPOST.objects.filter(article=post)
                if_liked=LOVEDPOST.objects.filter(jobseeker=obj,article=post)
                llen=len(if_liked)
                # print(llen)
                
                lovesize=len(lovedpost)
                comments=COMMENT.objects.filter(article=post)
                commentsize=len(comments)
                target_post.append([post,lovesize,commentsize,comments,llen])


            emp_i_should_follow=[]
            for emp in emp_reg:
                if emp.user.username not in emp_i_follow:
                    emp_i_should_follow.append(emp)
                if(len(emp_i_should_follow)>10):
                    break;    
            
            user_qual=QUALIFICATIONS.objects.get(user=request.user)
            recent_post_cnt=len(recent_posts)
            notifications=SHORTLISTED.objects.filter(applicant=obj,hasSeen=False)
            
            notlen=len(notifications)
            param={
                'jbasic':obj,
                'jqual':user_qual,
                'emp_i_should_follow':emp_i_should_follow,
                # 'recent_posts':recent_posts,
                'recent_posts':target_post,
                'recent_post_cnt':recent_post_cnt,
                'notlen':notlen,
            }
           

            return render(request,'JOBSEEKER/home.html/',param)
        #if not a valid user
        except:
            # return HttpResponse("NOT vALID  JS")
            return redirect('/')
                 
    

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

def follow_employee(request):
    # if an anoynmous barged in
    if not request.user.is_authenticated:
        return redirect('/')
    #valid barged in
    try:
        logged_in=request.user
        
        jobseeker=JOBSEEKER.objects.get(user=logged_in)
        logged_in_user=logged_in.username
        
        emp_reg=EMPLOYER.objects.all()
        emp_obj_follow=Follow.objects.filter(job_seeker=logged_in_user)
        emp_i_follow=[]
        for emp in emp_obj_follow:
            emp_i_follow.append(emp.employer)

        emp_i_should_follow=[]
        for emp in emp_reg:
                if emp.user.username not in emp_i_follow:
                    followers=Follow.objects.filter(employer=emp.user.username)
                    follower_len=len(followers)
                    emp_i_should_follow.append([emp,follower_len])

        notifications=SHORTLISTED.objects.filter(applicant=jobseeker,hasSeen=False)
            
        notlen=len(notifications)   
        param={
            'employees':emp_i_should_follow,
            'notlen':notlen,
        }

        


        return render(request,"JOBSEEKER/follow-employee.html/",param)
    except Exception as e:
        print(e)
        return redirect('/')    
        
     
    return render(request,"JOBSEEKER/follow-employee.html/")


def mymsg(request):
    
    user=User.objects.get(username=request.user)
    jobseeker=JOBSEEKER.objects.get(user=user)
    notications=SHORTLISTED.objects.filter(applicant=jobseeker,hasSeen=False)
    for noti in notications:
        noti.hasSeen=True
        noti.save()
    notification=SHORTLISTED.objects.filter(applicant=jobseeker).order_by('-id')
    # print(notification)
    param={
        'notifications':notification
    }
    return render(request,"JOBSEEKER/notifications.html/",param)

def prepare(request):
    if request.user.is_authenticated:
        try:
            jobseeker=JOBSEEKER.objects.get(user=request.user)
            notifications=SHORTLISTED.objects.filter(applicant=jobseeker,hasSeen=False)
            notlen=len(notifications)
            param={
                'notlen':notlen,
            }
            return render(request,"JOBSEEKER/preparation.html/",param)


        except:
            return redirect('/')    

    else:
        return redirect('/')    

def search(request):
    if request.method=='POST':
        curr_user=request.user.username
        # jobseeker=JOBSEEKER.objects.get(user=request.user)
        queryname=request.POST.get('searchquery')
        finalquery=queryname.lower()
        employers=EMPLOYER.objects.all()
        emp_i_follow=Follow.objects.filter(job_seeker=curr_user)
        print(emp_i_follow)
        emp_list=[]
        for emp in emp_i_follow:
            # print(emp.employer)
            emp_list.append(emp.employer)

        # print(emp_list)    
        suitableemployer=[]
        for emp in employers:
            if finalquery in emp.name.lower() and emp.user.username not in emp_list:
                suitableemployer.append(emp)

        # print(suitableemployer)
        emplen=len(suitableemployer)
        param={
            'emplen':emplen,
            'employers':suitableemployer,
            'query':queryname,
        }
        return render(request,"JOBSEEKER/searchresults.html/",param)
        
    else:
        return redirect('/')    


def handlelogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return redirect('/')            

def handlecomment(request):
    if request.method=='POST':
        jobseeker=JOBSEEKER.objects.get(user=request.user)


        message=request.POST.get('message')
        article_id=request.POST.get('article_id')
        article=ARTICLE.objects.get(article_id=article_id)
        new_msg=COMMENT.objects.create(jobseeker=jobseeker,article=article,commenttext=message)
        # print(message,article,jobseeker)
        
        data={
            'is_ok':1
        }
        return JsonResponse(data)



    else:
        return redirect('/')    


def lovepost(request):
    if request.user.is_authenticated:
        jobseeker=JOBSEEKER.objects.get(user=request.user)
        article_id=request.GET.get('article_id')
        article=ARTICLE.objects.get(article_id=article_id)
        new_like=LOVEDPOST.objects.create(jobseeker=jobseeker,article=article)
        data={
            'is-ok':1,
        }
        return JsonResponse(data)
    else:
        return redirect('/')    

def profile(request):
    # return HttpResponse("edit profile")
    jobseeker=JOBSEEKER.objects.get(user=request.user)
    qualification=QUALIFICATIONS.objects.get(user=request.user)
    notifications=SHORTLISTED.objects.filter(applicant=jobseeker,hasSeen=False)
    notlen=len(notifications)
    
    
    param={
        'notlen':notlen,
        'jobseeker':jobseeker,
        'qualification':qualification,
       
    }
    return render(request,'JOBSEEKER/profile.html/',param)


def editprofile(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            
            jobseeker=JOBSEEKER.objects.get(user=request.user)
            qualification=QUALIFICATIONS.objects.get(user=request.user)
            first_name=request.POST.get('jFirstName',None)
            last_name=request.POST.get('jLastName',None)
            email=request.POST.get('jemail',None)
            x_marks=request.POST.get('jXmarks')
            xii_marks=request.POST.get('jXiimarks')
            grad_marks =request.POST.get('jGradmarks')
            
            phone=request.POST.get('jPhone')
            profile_pic=request.FILES.get('jProfilePic',None)
            resume=request.FILES.get('jResume',None)
            jobseeker.first_name=first_name
            jobseeker.last_name=last_name
            jobseeker.email=email
            jobseeker.phone=phone
            qualification.x_marks=x_marks
            qualification.xii_marks=xii_marks
            qualification.grad_marks=grad_marks
            if profile_pic is not None:
                qualification.profile_pic=profile_pic
            if resume is not None:
                qualification.resume=resume

            jobseeker.save()
            qualification.save()        
            # print(first_name,last_name,email,x_marks,xii_marks,grad_marks,phone)
            return redirect('/JOBSEEKER/profile/')

        jobseeker=JOBSEEKER.objects.get(user=request.user)
        qualification=QUALIFICATIONS.objects.get(user=request.user)
        param={
            'jobseeker':jobseeker,
            'qualification':qualification,
        }
        return render(request,'JOBSEEKER/edit-profile.html/',param)
    else:
        return redirect('/')    