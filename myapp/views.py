import json

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from requests.auth import HTTPBasicAuth

#from myapp.forms import employeeform
#from myapp.models import employee
from myapp.models import Member, Products, ImageModel
from myapp.forms import ProductsForm, ImageUploadForm
from myapp.credentials import MpesaC2bCredential, MpesaAccessToken, LipanaMpesaPpassword

# Create your views here.

def gallery(request):
    return  render(request, 'gallery.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return  render(request,'about.html')
def inner(request):
    return render(request,'inner-page.html')
def department(request):
    return render(request, 'department.html')
def doctors(request):
    return  render(request, 'doctors.html')






#def service(request):
   # members = employee.objects.all()
    #return render(request, 'service.html', {'all':members})

def registration(request):
    if request.method == 'POST':
        members =Member(firstname=request.POST['firstname'],lastname=request.POST['lastname'],email=request.POST['email'],
                        username=request.POST['username'], password=request.POST['password'])
        members.save()
        return redirect('/')
    else:
         return render(request, 'registration.html')
def login(request):
    return render(request, 'login.html')

def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],
                                 password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'],
                                        password=request.POST['password'])
            return render(request, 'index.html',{'member': member})
        else:
            return render(request, 'login.html')
    else:
         return render(request, 'login.html')


    return render(request, 'index.html')


def service(request):
    return render(request, 'service.html')
def pricing(request):
    return render(request, 'pricing.html')
def testmonials(request):
    return render(request, 'testimonials.html')
def questions(request):
    return render(request, 'frequentlyaskedquestions.html')
def add(request):
    if request.method == "POST":
        form =ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductsForm()
        return render(request, 'addproducts.html', {'form':form})






def show(request):
    products = Products.objects.all()
    return render(request, 'show.html', {'products':products})


def delete(request, id):
    product = Products.objects.get(id = id)
    product.delete()
    return redirect('/show')

def edit(request, id):
    product = Products.objects.get(id = id)
    return render(request, 'edit.html', {'product':product})

def update(request, id):
    product = Products.objects.get(id = id)
    form = ProductsForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html', {'product':product})
def pay(request):
    return render(request,'pay.html')

# function that generates a token
def token(request):
    consumer_key = 'nnuypckGY97scmh2TZPqrgtBit5d17KU'
    consumer_secret = 'HtbS2lE3mrMieXiM'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

# returning stk push
def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Acer Enterprises",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Message sent successful")

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/image')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/image')