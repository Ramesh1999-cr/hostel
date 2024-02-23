

from django.shortcuts import render,redirect
from  django.contrib.auth.hashers import check_password,make_password
from django.core.mail import send_mail
from  django.contrib.auth.views import UserModel
from  django.http import response,JsonResponse
from  django.views import View
from  django.views.decorators.csrf import csrf_exempt,csrf_protect
from  floors.models import Register_user
from floors.serializer import Registerserializer
from django.http import HttpResponse

# Create your views here.


class userapp(View):

    @csrf_exempt
    def get(self,request,email=None):
        try:
            if request.method == "GET":
                if email:
                    reg_obj=Register_user.objects.get(email=email)
                    many=False
                else:
                    reg_obj = Register_user.objects.all()
                    many = True
                reg_obj= Registerserializer(reg_obj, many=many).data
                if reg_obj:
                    response= {'code':'200','massage':'success','data':reg_obj}

                else:
                    response= {'code':'400','massage':'NOT data found', 'data':{}}

            else:
                response={'code':'400','please check the method ':'false','data':{}}

        except Exception as e:
            print(e)
            response={'code':'500','massage':'false','data':{'errors':e}}

        return HttpResponse  (response)



    @csrf_exempt
    def post(self,request):
        try:
            if userapp :
                pass

        except:
            pass





