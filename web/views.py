from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Expense,Income,UserRegisterTemp,Token
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import string
import random
import smtplib
import requests


# Create your views here.

def rand_str(num=48):
    str = "".join(random.choice(string.ascii_letters+string.digits) for _ in range(num))
    return str

def send_mail(email,msg):
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.starttls()
    me ="soheilrasekh555@gmail.com"
    #TODO : / set password for smtp
    smtp.login(user=me,password="Changeit9!#&(&^%$#@!")
    smtp.sendmail(me,email,msg)
    smtp.quit()


@csrf_exempt
def register(request):
    data={}
    if request.method == "POST":
        username            = request.POST['username']
        password            = request.POST['password']
        password_confirm    = request.POST['password-confirm']
        email               = request.POST['email']
        code                = rand_str(20)


        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
            }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        ''' End reCAPTCHA validation '''

        email_exist     = User.objects.filter(email = email).exists()
        username_exist  = User.objects.filter(username = username).exists()

        sent = False
        if not email_exist and not username_exist and result['success'] and password == password_confirm:
            UserRegisterTemp.objects.create(username = username ,password =password, email = email, code=code )
            mail = """ please enter this  link to confirm your account : http://127.0.0.1:8000/register?key="""+code
            send_mail(email,mail)
            msg = "Link sent to your email please check it out."
            sent = True
        else:
            msg = "your email address or your username exists in our database or your are a Robot or your  password does not match each other"

        data={"msg":msg,"sent":sent}

        return render(request,"register.html",data)



    elif request.method == "GET":
        if request.GET.get("key"):
            code = request.GET.get('key')
            if UserRegisterTemp.objects.filter(code = code).exists():
                user = UserRegisterTemp.objects.get(code=code)
                newuser = User.objects.create(username = user.username , password = user.password , email= user.email)
                token = rand_str()
                Token.objects.create(user=newuser,token=token)
                user.delete()
                msg = "hello your token is {} please save it cause it can not resored at this time".format(token)
                sent = True
            else:
                msg= "your key is invalid"
                sent = False
            data={"msg":msg,"sent":sent}



        return render(request,"register.html",data)


    return render(request,"register.html",data)






def home_view(request):
    return render(request,"home.html",{})


def about_view(request):
    return render(request,"about.html",{})




@csrf_exempt
def submit_expense(request):
    data = {"type":"expense"}
    if request.method == "POST":
        text = request.POST['text']
        amount = request.POST['amount']
        token = request.POST['token']

        user = User.objects.filter(token__token = token).get()
        Expense.objects.create(text=text,amount=amount,user=user)
        data['done'] = "Data sent ...."

    return render(request,"income_expense.html",data)


@csrf_exempt
def submit_income(request):
    data = {"type":"income"}
    if  request.method == "POST":
        text = request.POST['text']
        amount = request.POST['amount']
        token = request.POST['token']

        user = User.objects.filter(token__token = token).get()
        Income.objects.create(text=text,amount=amount,user=user)
        data['done'] = "Data sent ...."


    return render(request,"income_expense.html",data)
