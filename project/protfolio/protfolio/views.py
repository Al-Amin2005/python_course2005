from django.http import HttpResponse
from django.shortcuts import render,redirect

from . models import About
from django.contrib import messages

import re


def demo(request):
    title = "this is a demo html"
    name = "Alamin"
    product_name = ['p1','p2','p3']
    data = {"t":title,'name':name,'prod':product_name}
    # print("this is root url function")
    return render(request,'protfolio.html',data)

def demo1(request):
    a = 10
    b = 20
    c = a + b
    # print("this is root url function")
    return HttpResponse(c)


def about_index(request):

    all_data = About.objects.all()
    
    msg = messages.get_messages(request)
    print(msg)

    data = {'d':all_data,'msg':msg }
    # print("this is root url function")
    return render(request,'admin/about.html',data)

from datetime import datetime

def about_insert(request):

    name = request.POST.get('uname')
    dob = request.POST.get('dob')
    phone = request.POST.get('phone') 
    email = request.POST.get('email')
    exp = request.POST.get('exp')
    no_cust = request.POST.get('no_cust')
    no_project = request.POST.get('no_project')
    no_of_awards = request.POST.get('no_of_awards')
    desc = request.POST.get('desc')
    current_date_time = datetime.now()
    formatted_date_time = current_date_time.strftime("%d %b %Y %I:%M %p")
    pattern = r"^[a-zA-Z0-9_.]+@gmail\.com$"

    # Check if any of the required fields is empty
    # if not all([name, dob, phone, email, exp, no_cust, no_project, no_of_awards, desc]):
        # messages.success(request,"The field can not be empty")
        # return HttpResponse("Error: All fields are required")
    # else:
    if not re.match(pattern, email):
            messages.success(request,"you email is not gmail")
    else:


        about_obj = About()
 
        about_obj.u_name = name
        about_obj.dob = dob
        about_obj.phone = phone
        about_obj.email = email
        about_obj.no_exp = exp
        about_obj.no_happy_customers = no_cust
        about_obj.no_project_finished = no_project
        about_obj.no_digital_awards = no_of_awards
        about_obj.discription = desc
        about_obj.date_time =formatted_date_time
       
        about_obj.save()
       


    #   print("this is root url function")
    return redirect('about')

def edit_index(request,id):

    data = About.objects.get(id=id)
    d = {'data':data}
    return render(request,'admin/edit.html',d)

def about_edit(request):
     
    id = request.POST.get('id')
    name = request.POST.get('uname')
    dob = request.POST.get('dob')
    phone = request.POST.get('phone') 
    email = request.POST.get('email')
    exp = request.POST.get('exp')
    no_cust = request.POST.get('no_cust')
    no_project = request.POST.get('no_project')
    no_of_awards = request.POST.get('no_of_awards')
    desc = request.POST.get('desc')
    current_date_time = datetime.now()
    # formatted_date_time = current_date_time.strftime("%d %b %Y %I:%M %p")

    about_obj = About.objects.get(id=id)

    about_obj.u_name = name
    about_obj.dob = dob
    about_obj.phone = phone
    about_obj.email = email
    about_obj.no_exp = exp
    about_obj.no_happy_customers = no_cust
    about_obj.no_project_finished = no_project
    about_obj.no_digital_awards = no_of_awards
    about_obj.discription = desc
    # about_obj.date_time =formatted_date_time
    
    about_obj.save()

    #   print("this is root url function")
    return redirect('about')

def delete_index(request,id):

    data = About.objects.get(id=id)
    data.delete()
    return redirect('about')