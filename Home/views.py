from django.shortcuts import render,redirect
# Create your views here.

from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

class home(TemplateView):
	template_name='INDEXYZ.html'

class About(TemplateView):
	template_name='About.html'

class contact(TemplateView):
	template_name='CONTACT,html.html'

class learn(TemplateView):
	template_name='learn.html'

class compare(TemplateView):
	template_name='compare.html'

class haveques(TemplateView):
	template_name='haveques.html'





 
           

	
	





































































































	