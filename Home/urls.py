from django.urls import path
from . import views

urlpatterns=[
path('',views.home.as_view(),name='home'),
path('About/',views.About.as_view(),name='About'),
path('CONTACT,html.html',views.contact.as_view(),name='contact'),
path('learn.html',views.learn.as_view(),name='learn'),
path('compare.html',views.compare.as_view(),name='compare'),
path('haveques.html',views.haveques.as_view(),name='haveques'),
]