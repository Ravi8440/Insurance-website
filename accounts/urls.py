from django.urls import path
from . import views

urlpatterns=[
path('createacc/',views.createacc,name='createacc'),
path('login/',views.Login,name='Login'),
path('Logout/',views.logout,name='logout'),
]