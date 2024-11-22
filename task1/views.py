from django.shortcuts import render, redirect
from task1.forms import UserRegister
from django.http import HttpResponse
from .models import *


# Create your views here.
def menu(request):
    return render(request, 'menu.html')


# def game(request):
#     game1 = 'Atomic Heart'
#     game2 = 'Cyberpunk 2077'
#     game3 = 'PayDay'
#     context = {'game1': game1,
#                'game2': game2,
#                'game3': game3
#                }
#     return render(request, 'fourth_task/games.html', context)

def game(request):
    Games = Game.objects.all()
    context = {'Games': Games
               }
    return render(request, 'games.html', context)


def cart(request):
    return render(request, 'cart.html')


def platform(request):
    return render(request, 'platform.html')


def sign_up_by_django(request):
    info = {}
    Buyer.objects.all()  # получаем данные из БД
    if request.method == 'POST':  # проверка запроса на GET или POST
        form = UserRegister(request.POST)  # создаем форму с данными
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if repeat_password != password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                # Здесь можно сохранить данные, если есть модель
                buyer = Buyer.objects.create(name=username, age=age, balance=0)  # сохраняем нового пользователя в базу данных
                return redirect('platform/')  # Перенаправление на именованный маршрут
    else:
        form = UserRegister()  # если метод запроса не 'POST', то создаем пустую форму
        print('GET запрос')
    info['form'] = form
    return render(request, 'registration_page.html', context=info)


def sign_up_by_html(request):
    users = ['teammate', 'pilot', 'fruit', 'spb1812']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if repeat_password != password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            return HttpResponse(f'Приветствуем тебя,{username}!')
    return render(request, 'registration_page.html', context=info)