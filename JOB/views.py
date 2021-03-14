from django.shortcuts import render,HttpResponse,redirect
from JOBSEEKER.models import JOBSEEKER,QUALIFICATIONS
from EMPLOYER.models import EMPLOYER
from django.contrib.auth.models import User
from .models import JOB,JOB_APPLICATIONS,APPLICATIONS,SHORTLISTED
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
            jobseeker=JOBSEEKER.objects.get(user=request.user)
            all_jobs=JOB.objects.all()
            jobs_applied=APPLICATIONS.objects.filter(applicant=jobseeker)
            jobs_shortlisted=SHORTLISTED.objects.filter(applicant=jobseeker)
            my_jobs=[]
            for job in jobs_applied:
                my_jobs.append(job.applicant_job)
            for job in jobs_shortlisted:
                my_jobs.append(job.applicant_job)
            qualification=QUALIFICATIONS.objects.get(user=request.user)
            valid_job=[]
            for job in all_jobs:
                if job not in my_jobs:
                    if job.x_req<=qualification.x_marks and job.xii_req<=qualification.xii_marks and job.grad_req<=qualification.grad_marks:
                        valid_job.append(job)


            # print(valid_job)
            len_count=len(valid_job)
            notifications=SHORTLISTED.objects.filter(applicant=jobseeker,hasSeen=False)
            
            notlen=len(notifications)
            params={
                'jobs':valid_job,
                'len':len_count,
                'notlen':notlen,
            }
            return render(request,'JOBSEEKER/relevant-jobs.html/',params)





            #old code
            # valid_jobseeker=QUALIFICATIONS.objects.get(user=logged_in)
            # applied_in=JOB_APPLICATIONS.objects.filter(jobseeker_username=logged_in.username)
            # # print(applied_in)
            # applied_job_id=[]
            # for jb in applied_in:
            #     applied_job_id.append(jb.job_id)

            # jobs=JOB.objects.all()
            # suitable_jobs=[]
            # for job in jobs:
            #     if job.x_req <= valid_jobseeker.x_marks and job.xii_req <= valid_jobseeker.xii_marks and job.grad_req <= valid_jobseeker.grad_marks and job.job_id not in applied_job_id :

            #         suitable_jobs.append(job)
            # len_count=len(suitable_jobs)        
            # params={
            #     'jobs':suitable_jobs,
            #     'len':len_count,
            # }
            # return render(request,'JOBSEEKER/relevant-jobs.html/',params)
            
        except Exception as e:
            print(e)
            return redirect("/")    
        
        
        
def job_application(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        applied_job_id=request.GET.get('job_id')  
        #delete area begin  
        # new_application=JOB_APPLICATIONS(job_id=applied_job_id,jobseeker_username=request.user.username)

        

        # new_application.save()
        #delete area end
        applicant=JOBSEEKER.objects.get(user=request.user)
        job_num=JOB.objects.get(job_id=applied_job_id)
        application=APPLICATIONS(applicant=applicant,applicant_job=job_num)
        application.save()
        data={
            'is_ok':1,
        }
        return JsonResponse(data)