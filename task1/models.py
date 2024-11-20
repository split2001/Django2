from django.db import models

# Create your models here.
# каждый класс это отдельная таблица


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=100, decimal_places=3)
    age = models.IntegerField()


class Game(models.Model):
    title = models.CharField(max_length=100)

    cost = models.DecimalField(max_digits=100, decimal_places=3)

    size = models.DecimalField(max_digits=100, decimal_places=3)  # размер файлов игры

    description = models.TextField()  # неограниченное количество текста

    age_limited = models.BooleanField(default=False)

    buyer = models.ManyToManyField(Buyer)  # связь с моделью Buyer

