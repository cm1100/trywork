from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'device'
urlpatterns = [
   path("",views.HomePage.as_view(),name="home"),
   path("getlist/",views.GetList.as_view(),name="getlist")
]