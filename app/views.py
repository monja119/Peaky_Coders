from django.shortcuts import render, redirect
from django.http import HttpResponse, request


class Tabs:
    def data(self, request):
        msg = "Views1"
        return render(request, 'tabs/data.html', locals())

    def recyclage(self, request):
        msg = "Views2"
        return Httpresponse(msg)

    def bin(self, request):
        msg = "Views3"
        return Httpresponse(msg)

    def extra(self, request):
        msg = "Views4"
        return Httpresponse(msg)
