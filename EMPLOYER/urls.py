from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('home/',views.home,name="home"),
    path('registeremployer/',views.registeremployer,name="register employer"),
    path('publish-post/',views.publishpost,name="publish post"),
    path('my-jobs/',views.myjobs,name="my jobs"),
    path('publish-jobs/',views.publishjobs,name="publish job"),
    path('delete-job/',views.deletejob,name="delete-job"),
    path('applied-candidate/',views.candidateapplied,name="candidates application"),
    path('receive-response/<str:slug>/<int:id>/',views.receiveresponse,name="receive response"),
    path('delete-article/article/<int:id>/',views.deletepost,name="delete_post"),
]
