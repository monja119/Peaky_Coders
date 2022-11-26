from django.http import HttpResponse
from django.shortcuts import render
import email
import imaplib
from email.header import decode_header


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
    
    def delete_email(request):
        
        msg = "Views3"
        return Httpresponse(msg)
    
    def views4(request):
        msg = "Views4"
        return Httpresponse(msg)
    
    def views5(request):
        msg = "Views5"
        return Httpresponse(msg)