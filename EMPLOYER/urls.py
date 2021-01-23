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
    path('delete-article/article/<int:id>/',views.deletepost,name="delete_post"),
]
