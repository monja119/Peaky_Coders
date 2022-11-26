from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Class1.views1, name='name1'),
    path('page1/', views.Class1.views2, name='name2'),
    path('page2/', views.Class1.views3, name='name3'),
    path('page3/', views.Class1.views4, name='name4'),
]
