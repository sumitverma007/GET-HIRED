from django.shortcuts import render,HttpResponse,redirect
from .models import EMPLOYER
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
            print("Valid Employer")
            #design Home page for Employer
            return HttpResponse("Valid Employer")
        except:
            print("Not a valid Employer")
            return redirect('/')    

