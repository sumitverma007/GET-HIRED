from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('home/',views.home,name="home"),
    path('registerjobseeker/',views.registerjobseeker,name="jobseeker reg"),
    path('follow-employee/',views.follow_employee,name="follow employee"),
    path('messages/',views.mymsg,name="notification"),
    path('prepare/',views.prepare,name="preparation",)
]
