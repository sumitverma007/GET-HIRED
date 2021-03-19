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
    path('prepare/',views.prepare,name="preparation"),
    path('search/',views.search,name="querysearch"),
    path('handle_comment/',views.handlecomment,name="comment-publish"),
    path('handlelove/',views.lovepost,name="postlove"),
    path('handlelogout/',views.handlelogout,name="logout"),
]
