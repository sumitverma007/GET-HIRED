from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.indexhome,name="home"),
    path('handlelogin/',views.handlelogin,name="login"),
    path('BASE/handleuser/',views.handleuser,name="handleuser"),
]
