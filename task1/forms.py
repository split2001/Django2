from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин:', required=True, widget=forms.TextInput)
    password = forms.CharField(min_length=8, label='Введите пароль:', required=True, widget=forms.PasswordInput)
    repeat_password = forms.CharField(min_length=8, label='Повторите пароль:', required=True, widget=forms.PasswordInput)
    age = forms.IntegerField(max_value=100, label='Введите возраст:', required=True)


