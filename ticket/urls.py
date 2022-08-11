from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
        path('',views.index,name='index'),
        path('users/new',views.authorize,name='authorize'),
        path('tickets/new',views.raiseticket,name='raiseticket'),
       

]


