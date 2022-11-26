from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



class Class1:
    '''
       ********** 
    '''
    
    def views1(request):
        msg = "Views1"
        return Httpresponse(msg)
    
    def views2(request):
        msg = "Views2"
        return Httpresponse(msg)
    
    def views3(request):
        msg = "Views3"
        return Httpresponse(msg)
    