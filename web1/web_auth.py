from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from form import LoginUserForm, RegisterUserForm
from web1.form import *


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')

    else:
        form = LoginUserForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

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