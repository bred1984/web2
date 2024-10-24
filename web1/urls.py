"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

# import views
# import web_auth
# from web.web1 import views
# from views import *
from web1 import views
from web1 import web_auth
urlpatterns = [
    path('',views.index, name='home'),
    path('user',views.foo),
    path('user/<name>',views.foo),
    path('user/<name>/<age>',views.foo),
    # path('adduser',views.InsertUserDB,name='adduser'),
    path('createdb',views.CreateDB, name='createdb'),
    path('showuser',views.ShowUser,name='showuser'),
    path('showphoto',views.ShowPhoto,name='showphoto'),
    path('addphoto',views.AddPhoto,name='addphoto'),
    path('chat',views.Chat,name='chat'),
    path('ajax', views.Ajax, name='ajax'),
    path('getajax', views.GetAjax, name = 'getajax'),
    path('login', web_auth.login_user, name='login'),
    path('logout', web_auth.logout_user, name='logout'),
    path('register', web_auth.register, name='register'),
]
