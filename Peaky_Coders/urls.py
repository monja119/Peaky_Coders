from django.contrib import admin
from django.urls import path, re_path
from app.views import *
from app.modules import *

tab = Tabs()
user = UserView()


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^home/$', tab.base, name='base'),
    re_path('^$', tab.home, name='home'),
    re_path('^data/$', tab.data, name='data'),
    re_path('^recyclage/$', tab.recyclage, name='recyclage'),
    re_path('^bin/$', tab.bin, name='bin'),
    re_path('^extra/$', tab.extra, name='extra'),

    # user
    re_path('^user/login/$', user.login, name='login'),
    re_path('^user/register/$', user.register, name='register'),
    re_path('^user/logout/$', user.logout, name='logout'),

    # recyclage
    re_path('^recycle/share/$', Recycle().share, name='shareRecycle'),
    re_path('^recycle/question/$', Recycle().question, name='questionRecycle'),

    # MODULES
    # email
    re_path('^module/email/$', EmailModule().home, name='emailModule'),
    re_path('^module/email/delete/$', EmailModule().delete_email_list, name='emailDeleteModule'),
    re_path('^module/email/add/', EmailModule().add_mail, name='emailAddModule'),

    # compressor
    re_path('^module/compressor/', CompressorModule().add_file, name='compressorAddFileAddModule'),



]
