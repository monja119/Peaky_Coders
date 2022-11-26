from django.contrib import admin
from django.urls import path, re_path
from app.views import Tabs

tab = Tabs()

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$', tab.home, name='home'),
    re_path('^data/$', tab.data, name='data'),
    re_path('^recyclage/$', tab.recyclage, name='recyclage'),
    re_path('^bin/$', tab.bin, name='bin'),
    re_path('^extra/$', tab.extra, name='extra'),

]
