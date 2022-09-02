import json

from django.shortcuts import render
from django.views import View
import requests
from django.conf import settings
# Create your views here.


class HomePage(View):

    def get(self,request):

        ctx = {}
        return render(request,"device/home.html",ctx)

    def post(self,request):
        try:
            data = request.POST.get('textarea1',None)
            response = requests.post(settings.API_HIT,json.dumps(data))
            if response.status_code==200:
                ctx = {"message":"succesfully added","error":False}
                return render(request,"device/home.html",ctx)
            response = json.loads(response.content)
            ctx = {'message':str(response),"error":True}
            return render(request, "device/home.html", ctx)
        except Exception as e:
            ctx = {'message': str(e), "error": True}
            return render(request, "device/home.html", ctx)


class GetList(View):

    def get(self,request):


        try:
            response =requests.get(url=settings.GET_API)
            if response.status_code==200:
                list_objs = json.loads(response.content)
                ctx = {'list_objs':list_objs}
                return render(request,"device/home.html",ctx)
            response = json.loads(response.content)
            ctx = {'message':str(response),'error':True}
            return render(request,'device/home.html',ctx)
        except Exception as e:
            ctx = {'message': str(e), "error": True}
            return render(request, "device/home.html", ctx)










