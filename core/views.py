from django.shortcuts import redirect, render
import core.serializers as sr
import core.models as md
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics,views, response
import random
from core.forms import IQ_Test_Form, EQ_Test_Form
# Create your views here.


def new_login():
    string=""
    for i in range(10):
        string+=chr(random.randint(97,122))
    return string

class Login_API(views.APIView):
    def get(self,request):
        string=new_login()
        while md.Unique_Login.objects.filter(login=string).exists():
            string=new_login()
        md.Unique_Login.objects.create(login=string)
        return response.Response({"operation":"succes","new_login":md.Unique_Login.objects.last().login})

@api_view(["POST"])
def get_login_test(request):
    if request.method=="POST":
        obj=md.Unique_Login.objects.get(login=request.data["login"])
        ser=sr.Unique_Login_Serializer(obj)
        iq_data=md.IQ_Test.objects.get(login_f=ser.data["id"])
        iq_ser=sr.IQ_Serializer(iq_data)
        eq_data=md.EQ_Test.objects.get(login_f=ser.data["id"])
        eq_ser=sr.EQ_Serializer(eq_data)
        return response.Response({"iq_score":iq_ser.data["score"],"iq_time":iq_ser.data["date_passed"],"eq_score":eq_ser.data["result"],"eq_time":eq_ser.data["date_passed"],"login":eq_ser.data["login_f"]})
        
class IQ_API(views.APIView):
    def post(self,request):
        ser=sr.IQ_Serializer(data=request.data)
        try:
            ser.is_valid(raise_exception=True)
            ser.save()
        except Exception as e:
            return response.Response({"operation":"failed","error":e.args})
        return response.Response(ser.data,status=status.HTTP_201_CREATED)
class EQ_API(views.APIView):
    def post(self,request):
        ser=sr.EQ_Serializer(data=request.data)
        try:
            ser.is_valid(raise_exception=True)
            ser.save()
        except Exception as e:
            return response.Response({"operation":"failed","error":e.args})
        return response.Response(ser.data,status=status.HTTP_201_CREATED)


def login_get(request):
    print(request)
    if request.method=="POST":
        if request.POST.get("get_login",False):
            string=new_login()
            while md.Unique_Login.objects.filter(login=string).exists():
                string=new_login()
            md.Unique_Login.objects.create(login=string)
            request.session["string"]=string
            return redirect("iq_test")
        send_login=request.POST["login_form"]
        request.session["string"]=send_login
        return redirect("finish")
    
    return render(request, "index.html")
def iq_test(request):
    if request.method=="POST":
        form=IQ_Test_Form(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            login=request.session.get("string")
            login=md.Unique_Login.objects.get(login=login)
            score=data.get("score")
            request.session["string"]=login.login
            md.IQ_Test.objects.create(score=score, login_f=login)
            return redirect("eq_test")
    login=request.session.get("string")
    form=IQ_Test_Form()
    return render(request, "iqtest.html",locals())

def eq_test(request):
    if request.method=="POST":
        form=EQ_Test_Form(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            login=request.session.get("string")
            login=md.Unique_Login.objects.get(login=login)
            result=data.get("result")
            request.session["string"]=login.login
            md.EQ_Test.objects.create(result=result, login_f=login)
            return redirect("finish")
    form=EQ_Test_Form()
    login=request.session.get("string")
    return render(request, "eqtest.html",locals())

def finish_page(request):
    login=md.Unique_Login.objects.get(login=request.session.get("string"))
    test_score=login.iq_test.score
    test_result=login.eq_test.result
    time_iq=login.iq_test.date_passed
    time_eq=login.eq_test.date_passed
    login=login.login
    return render(request, "finish.html",locals())