from django.contrib import admin
from django.urls import path, include

from dummyapp import views
from dummyapp.views import demo

urlpatterns = [
    path('',views.demo,name='demo'),
    path('add/',views.operations,name='operations'),
]