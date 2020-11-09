from django.shortcuts import render,redirect
# Create your views here.

from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponse
from django.urls import path,include

# Create your views here.

def createacc(request):
	if request.method =='POST':
		fpassword=request.POST.get('password')
		fconf_pass=request.POST.get('conf_password')

		if fpassword == fconf_pass:
			try:
				user =User.objects.get(username= request.POST['email'])
				return render(request, 'createacc.html',{'error':"Email has already been taken"})
			except User.DoesNotExist:
			    user = User.objects.create_user(username= request.POST['email'], first_name= request.POST['first'], last_name=request.POST['last'], password= request.POST['password'], email= request.POST['email'])
			    return redirect(Login)
		else:
		    return render(request,'createacc.html', {'error':"Password Don't Match"})
	else:
	    return render(request, 'createacc.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['password']

        user = auth.authenticate(username=email, password=pwd)

        if user is not None:
            auth.login(request,user)
            return render(request, 'INDEXYZ.html')

        else:
            return render(request,'Login.html',{'error': "Invalid Credentials"})

    else:
        return render(request,'Login.html')

def logout(request):
    auth.logout(request)
    return redirect(Login)