from django.urls import path

# import views
# import web_auth
# from web.web1 import views
# from views import *
from web2 import views
# from web2 import web_auth

urlpatterns = [
    path('',views.index, name=''),

]