from django import forms
from django.contrib.auth import get_user_model


class UserForm(forms.Form):
    name2='123'
    # def __init__(self,name1:str,age1):
    #     self.name1=name1
    #     self.age1=age1
    name = forms.CharField(initial='Введите имя')
    age = forms.IntegerField(initial='Введите возраст')
    pasport = forms.CharField(initial='Введите паспорт')

class ShowUserForm(forms.Form):
    name = forms.CharField(initial='Введите имя')

class AddPhotoForm(forms.Form):
    name=forms.ImageField(label="")

class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }