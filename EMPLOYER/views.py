from django.shortcuts import render,HttpResponse,redirect
from .models import EMPLOYER
from ARTICLE.models import ARTICLE
from JOB.models import JOB,JOB_APPLICATIONS,APPLICATIONS,SHORTLISTED
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from JOBSEEKER.models import JOBSEEKER,QUALIFICATIONS
from django.http import JsonResponse
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

def publishjobs(request):
    if request.method=='POST':
        employer=EMPLOYER.objects.get(user=request.user)
        job_title=request.POST.get('job_title')
        job_desc=request.POST.get('job_desc')
        x_req=request.POST.get('x_req')
        xii_req=request.POST.get('xii_req')
        grad_req=request.POST.get('grad_req')
        try:
            new_job=JOB(job_title=job_title,job_desc=job_desc,x_req=x_req,xii_req=xii_req,grad_req=grad_req,employer_name=employer)
            new_job.save()
            messages.success(request,"job published Successfully")
            return redirect('/EMPLOYER/my-jobs/')
        except:
            messages.error(request,"Failed to publish job.")
            return redirect('/EMPLOYER/my-jobs/')    
    

    else:
        return redirect('/')         

def deletejob(request):
    if request.method=='POST':
        job_id=request.POST.get('job-id')
        try:
            job_to_delete=JOB.objects.get(job_id=job_id)
            # job_applications=JOB_APPLICATIONS.objects.filter(job_id=job_id)
            # for application in job_applications:
            #     application.delete()
            job_to_delete.delete()

            messages.success(request,"Job deleted Successfully")

            data={
                'is_ok':1,
            }    
            return JsonResponse(data)
        except:
            data={
                'is_ok':0,
            }
            messages.error(request,"Failed to delete job")
            return JsonResponse(data)
    else:
        return redirect('/')    



def candidateapplied(request):
    if request.user.is_authenticated:
        #valid employer
        try:
            employer=EMPLOYER.objects.get(user=request.user)
            all_jobs=JOB.objects.filter(employer_name=employer)
            applications=[]
            # print(all_jobs)
            for job in all_jobs:
                applied=APPLICATIONS.objects.filter(applicant_job=job)
                if len(applied)>0:
                    applications.append(applied)
         
            
            param={
                'applications':applications,
            }
            
            

            return render(request,'EMPLOYER/applicants.html/',param)
          
        except Exception as e:
            #not valid employer
            print(e)
            return redirect('/')    
    else:

        return redirect('/')


def receiveresponse(request,slug,id):
    # print(slug,id)
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        # logged in 
        # check if jobseeker is here
        try:
            employer=EMPLOYER.objects.get(user=request.user)
            try:
                #check application
                applicant_user=User.objects.get(username=slug)
                qualification=QUALIFICATIONS.objects.get(user=applicant_user)
                applicant=JOBSEEKER.objects.get(user=applicant_user)
                
                job=JOB.objects.get(job_id=id)
                
                application=APPLICATIONS.objects.get(applicant=applicant,applicant_job=job)
                # check if job's employer is the one logged in 
                if job.employer_name==employer:
                    param={
                        'application':application,
                        'qualification':qualification,
                    }
                    return render(request,'EMPLOYER/send-response.html/',param)
                 
                else:
                    return redirect('/')
                  



                return HttpResponse("Valid application")
            except Exception as e:
                print(e)
                return redirect('/')    
        except Exception as e:
            print(e)
            return redirect('/')        

    return HttpResponse("Ohoy scoop")        


def acceptuser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        job_id=request.POST.get('job_id')
        msg=request.POST.get('msg')
        applicant_user=User.objects.get(username=username)
        applicant=JOBSEEKER.objects.get(user=applicant_user)
        job=JOB.objects.get(job_id=job_id)
        application=APPLICATIONS.objects.get(applicant=applicant,applicant_job=job)
        recruit=SHORTLISTED(applicant=applicant,applicant_job=job,message=msg)
        recruit.save()
        application.delete()
        data={
            'is_ok':1,
        }
        return JsonResponse(data)

    else:
        return redirect('/')    

         


def rejectuser(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        job_id=request.POST.get('job_id')
        msg=request.POST.get('msg')
        applicant_user=User.objects.get(username=username)
        applicant=JOBSEEKER.objects.get(user=applicant_user)
        job=JOB.objects.get(job_id=job_id)
        application=APPLICATIONS.objects.get(applicant=applicant,applicant_job=job)
        
        
        application.delete()
        data={
            'is_ok':1,
        }
        return JsonResponse(data)
              
        

    else:
        return redirect('/')             



def candidateshortlisted(request):
    if request.user.is_authenticated:
        #valid employer
        try:
            employer=EMPLOYER.objects.get(user=request.user)
            all_jobs=JOB.objects.filter(employer_name=employer)
            applications=[]
            for job in all_jobs:
                applied=SHORTLISTED.objects.filter(applicant_job=job)
                if len(applied)>0:
                    applications.append(applied)

            param={
                'applications':applications,
            }        
            return render(request,'EMPLOYER/shortlisted-candidates.html/',param)

        except:
            return redirect('/')    
        
    else:
        return redirect('/')    



def releaseuser(request):
    if request.user.is_authenticated:
        #if a valid employer
        try:
            employer=EMPLOYER.objects.get(user=request.user)
            #employer
            username=request.POST.get('username')
            job_id=request.POST.get('job_id')
            juser=User.objects.get(username=username)
            jobseeker=JOBSEEKER.objects.get(user=juser)
            job=JOB.objects.get(job_id=job_id)
            application=SHORTLISTED.objects.get(applicant=jobseeker,applicant_job=job)
            application.delete()
            data={
                'ok':1,
            }
            return JsonResponse(data)

        except Exception as e:
            print(e)
            return redirect('/')    
        


     

    else:
        return redirect('/')    
