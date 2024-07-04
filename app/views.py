from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method=='POST':
        data=request.POST
        Firstname=data['fname']
        Lastname=data['lname']
        email=data['email']
        what=data['what']
        phone=data['pnum']
        message=data['mess']
    
        reg=Restro(firstnm=Firstname,lastnm=Lastname,email=email,what=what,phone=phone,message=message)
        reg.save()
        # return HttpResponse("Message successfully sent") 
        messages.success(request,f" {Firstname} {Lastname}, successfully message sent")
    return render(request,'app/home.html')

def aboutus(request):
    return render(request,"app/aboutus.html")
def contactus(request):
    return render(request,"app/contactus.html")
def ourmenu(request):
    data1=Buff.objects.all()
    data2=Chicken.objects.all()
    data3=Veg.objects.all()
    return render(request,'app/ourmenu.html',{'data1':data1,'data2':data2,'data3':data3})


def ourservices(request):
    return render(request,"app/ourservices.html")
def allergyadvice(request):
    return render(request,"app/allergyadvice.html")

def footer(request):
    return render(request,'app/footer.html')
def buff(request):
    data1=Buff.objects.all()
    return render(request,'app/buff.html',{'data1':data1})

def chicken(request):
    data2=Chicken.objects.all()
    return render(request,'app/chicken.html',{'data2':data2})

def veg(request):
    data3=Veg.objects.all()
    return render(request,'app/veg.html',{'data3':data3})