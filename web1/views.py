import json
from http.client import responses
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
# from SqlDriver import SqlDriver
# from form import UserForm, ShowUserForm, AddPhotoForm

from web1.SqlDriver import *
from web1.form import *

import os

# from web.web1.SqlDriver import SqlDriver
# from web.web1.form import AddPhotoForm, UserForm, ShowUserForm


def handle_uploaded_file(f,fulldir):
    # p=os.path.join(dir,f.name)
    # print(p)
    # with open(f"static/images/{f.name}", "wb+") as destination:
    with open(fulldir, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def index(request:HttpRequest):

    print(request.session)
    print(request.COOKIES)
    return render(request, "test1.html")

def foo(request:HttpRequest,name='Будеш хуй',age=20):
    print(request.get_full_path())
    print(request.get_host())
    print(request.get_port())
    # print(user)
    return HttpResponse(f'Имя {name}: возраст {age}')

def AddPhoto(request:HttpRequest):
    print(request.POST)
    if request.method=='POST':
        # handle_uploaded_file(request.FILES['file_upload'])
        print(request.POST)
        print(request.FILES)
        print(request.user)
        # handle_uploaded_file(request.FILES['name'])
        form = AddPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            # data={'zapros':'photo'}
            # print(SqlDriver.connect(SqlDriver.Show, data))
            # id = SqlDriver.connect(SqlDriver.Show, data)[len(SqlDriver.connect(SqlDriver.Show, data))-1]['id']
            # print('id',id)
            dir=f"images"
            fff=str(request.FILES['name'].name)
            SqlDriver.sql = f'select id from photo'
            if len(SqlDriver.connect(SqlDriver.Show))==0:
                print(request.FILES['name'].name)
                id=1
            else:
                id = SqlDriver.connect(SqlDriver.Show)[len(SqlDriver.connect(SqlDriver.Show)) - 1]['id']+1

            f=f'{id}.{fff.split('.')[1]}'
            print(f)
            fulldir=os.path.join(os.path.join('static',dir),f)
            print(fulldir)
            SqlDriver.sql=f"select id from auth_user where username = '{request.user}'"

            print(SqlDriver.sql)
            print(SqlDriver.connect(SqlDriver.Show))
            user_id=SqlDriver.connect(SqlDriver.Show)[0]['id']
            print(user_id)

            SqlDriver.sql=f"insert into photo (name, href, user_id) values('{fff}','{os.path.join(dir,f)}', '{user_id}')"
            SqlDriver.connect(SqlDriver.Insert_db)
            handle_uploaded_file(request.FILES['name'],fulldir)

            # handle_uploaded_file(request.FILES['name'],'')
            # handle_uploaded_file(form.cleaned_data['file'])
        # return render(request,'addphoto.html',{'form':form})
    else:
        form=AddPhotoForm()
    return render(request,'addphoto.html',{'form':form})

def ShowPhoto(request:HttpRequest):
    SqlDriver.sql = f"select name, href from photo where user_id = (select id from auth_user where username = '{request.user}')"
    data=SqlDriver.connect(SqlDriver.Show)
    print(data)
    dd=[]
    for d in data:
        dd.append(dict(d))
    print(dd)

    return render(request,'showphoto.html' , {'data':dd} )


# def InsertUserDB(request:HttpRequest):
#     if request.method=='POST':
#         form=UserForm(request.POST)#
#         if form.is_valid():
#             # form.cleaned_data['name']
#             # form.cleaned_data['age']
#             name=form.cleaned_data['name']
#             if ' ' in   name:
#                 return HttpResponse(' Дич')
#             form=UserForm()
#             print(request.POST)
#             data={}
#             data['fio']=request.POST.get('name')
#             data['age'] = request.POST.get('age')
#             data['pasport'] = request.POST.get('pasport')
#             status="Все ок"
#             # sql = SqlDriver()
#             # sql.connect(sql.insert_db,data)
#             SqlDriver.connect(SqlDriver.insert_db,data)
#
#             return render(request, 'adduser.html', {'form': form,'status':'Все ок'})
#         else:
#             return render(request, 'adduser.html', {'form': form,'status':'Не верно ввел'})
#
#     else:
#         form = UserForm()
#         return render(request,'adduser.html', {'form':form})

def CreateDB(request):
    SqlDriver.connect(SqlDriver.CreateDB)
    return HttpResponse('Таблицы созданы')


def ShowUser(request:HttpRequest):
    if request.method == 'POST':
        form=ShowUserForm()
        name=request.POST.get('name')
        print(name)
        SqlDriver.sql = f"select username from auth_user where username = '{name}'"
        res=SqlDriver.connect(SqlDriver.ShowUser)
        return render(request,'showuser.html', {'user':list(res),'form':form})
    else:
        SqlDriver.sql = f"select username from auth_user"
        res = SqlDriver.connect(SqlDriver.ShowUser )
        form = ShowUserForm()
        return render(request,'showuser.html', {'user':list(res),'form':form})


def Ajax(request:HttpRequest):
    #SqlDriver.sql = f"insert into chat (user1id, user2id, message) values ({}"
    # res = SqlDriver.connect(SqlDriver.ShowUser)
    info = json.loads(str(request.body, 'UTF-8'))
    print(info)
    print(info.get('id'))
    print(request.user)
    user_sql=f"select id from auth_user where username = '{request.user}'"
    print(user_sql)
    SqlDriver.sql=f"insert into chat(user1id, user2id, message) values (({user_sql}), {info.get('id')}, '{info.get('mes')}')"
    SqlDriver.connect(SqlDriver.Insert_db)
    response ={
        'data':'1234'
    }
    return JsonResponse(info)
def GetAjax(request:HttpRequest):
    info = json.loads(str(request.body, 'UTF-8'))
    print(info.get('id'))
    user_sql = f"select id from auth_user where username = '{request.user}'"
    # user_sql1 = f"select id from auth_user where username = '{request.user}'"
    SqlDriver.sql = f"select message from chat where (user1id = ({user_sql}) and user2id = '{info.get('id')}') "
    res = SqlDriver.connect(SqlDriver.ShowUser)
    print(res)
    # SqlDriver.sql = f"select message from chat where user2id = ({user_sql})"
    # res1 = SqlDriver.connect(SqlDriver.ShowUser)

    # print(list(res)[1]['message'])
    response = {'date':list(res)} #,'date1':list(res1)}
    return JsonResponse(response)
def Chat(request:HttpRequest):
    if request.method == 'POST':
        form=ShowUserForm()
        name=request.POST.get('name')
        id = request.POST.get('id')
        print(id,name)
        SqlDriver.sql = f"select username from auth_user where id = '{id}'"
        res=SqlDriver.connect(SqlDriver.ShowUser)
        return render(request,'chat.html', {'user':list(res),'form':form, 'user':name,'id':id})
    else:
        SqlDriver.sql = f"select id, username from auth_user where username != '{request.user}'"
        res = SqlDriver.connect(SqlDriver.ShowUser)
        form = ShowUserForm()
        return render(request,'userforchat.html', {'user':list(res),'form':form})
    # return render(request, 'userforchat.html')
    # return render(request, 'chat.html')
    # return render(request, 'chat2.html',{'form':form})



def Test(request):
    return render(request, 'test.html')



