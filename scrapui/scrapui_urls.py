
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.urls import path
from django.views.static import serve
from django.conf import settings
from scrapui.views import (
    Home,
    register,
    signin,
    profile,
    logoutuser,
    deactivate,


    addscrap,
    listscrap,
    editscrap,
    viewscrap,
    chat,
    contact ,
    blog ,
    feature ,
)

urlpatterns = [
    path('' , Home, name='home'),
    path('register/' , register , name='register') ,
    path('signin/' , signin , name='signin') ,
    path('profile/' , profile , name='profile') ,
    path('logout/' , logoutuser , name='logout') ,
    path('deactivate/' , deactivate , name='deactivate') ,


    path('scrap/' , addscrap , name='addscrap') ,
    path('listscrap/' , listscrap , name='listscrap') ,
    path('viewscrap/<int:id>/' , viewscrap , name='viewscrap') ,
    path('editscrap/<int:id>/' , editscrap , name='editscrap') ,

    path('contact/' , contact , name='contact'),
    path('blog/' , blog , name='blog') ,
    path('feature/' , feature , name='feature') ,


    path('bot/', chat , name='bot' ) ,


    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,})
]  +   static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)