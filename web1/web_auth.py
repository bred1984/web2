from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
# from form import LoginUserForm, RegisterUserForm
from web1.form import *
from django.contrib.sessions.models import Session
from web1.SqlDriver import *


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for session in Session.objects.all():
                raw_session = session.get_decoded()
                SqlDriver.sql = f"select id from auth_user where username = '{cd['username']}'"
                res = SqlDriver.connect(SqlDriver.ShowUser)
                id=res[0]['id']
                print(str(raw_session.get('_auth_user_id')), str(id))
                if str(raw_session.get('_auth_user_id'))==str(id) and ( str(raw_session.get('_auth_user_id')) !='1'):
                    print('adcsdvasfvasfv')
                    return HttpResponse('Сессия уже существуеет')
                # print()
                # uid = session.get_decoded().get('_auth_user_id')
                # if uid == TARGET_USER:  # this could be a list also if multiple users
                # print(session)
                # print(uid)
                print(raw_session)
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                # url_redirect = reverse('cats')
                return redirect('home')
                # return HttpResponseRedirect('web1/')

    else:
        form = LoginUserForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')
    # return HttpResponseRedirect('web1/')

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password']==form.cleaned_data['password2']:
                user = form.save(commit=False)  # создание объекта без сохранения в БД
                user.set_password(form.cleaned_data['password'])
                user.save()
                #return render(request, 'register_done.html')
                # return HttpResponse('Регистрация успешна')
                return HttpResponseRedirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})


# def goadmin(request):
#     return render(request, "test1.html", {'admin':1})
# def endadmin(request):
#     return render(request, "test1.html", {'admin':0})