from django.shortcuts import render,HttpResponse,redirect
from JOBSEEKER.models import JOBSEEKER,QUALIFICATIONS
from EMPLOYER.models import EMPLOYER
from django.contrib.auth.models import User
from .models import JOB,JOB_APPLICATIONS
from django.http import JsonResponse
# Create your views here.
def relevant_jobs(request):
    # return HttpResponse("Relevant Job page")
   
    
    if not request.user.is_authenticated:
        return redirect("/")
  
    
    else:
        # what if employer get in here
        logged_in = request.user
        try:
            valid_jobseeker=QUALIFICATIONS.objects.get(user=logged_in)
            applied_in=JOB_APPLICATIONS.objects.filter(jobseeker_username=logged_in.username)
            # print(applied_in)
            applied_job_id=[]
            for jb in applied_in:
                applied_job_id.append(jb.job_id)

            jobs=JOB.objects.all()
            suitable_jobs=[]
            for job in jobs:
                if job.x_req <= valid_jobseeker.x_marks and job.xii_req <= valid_jobseeker.xii_marks and job.grad_req <= valid_jobseeker.grad_marks and job.job_id not in applied_job_id :

                    suitable_jobs.append(job)
            len_count=len(suitable_jobs)        
            params={
                'jobs':suitable_jobs,
                'len':len_count,
            }
            return render(request,'JOBSEEKER/relevant-jobs.html/',params)
            
        except Exception as e:
            print(e)
            return redirect("/")    
        
        
        
def job_application(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        applied_job_id=request.GET.get('job_id')    
        new_application=JOB_APPLICATIONS(job_id=applied_job_id,jobseeker_username=request.user.username)
        new_application.save()
        data={
            'is_ok':1,
        }
        return JsonResponse(data)