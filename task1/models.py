from django.db import models

# Create your models here.
# каждый класс это отдельная таблица


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=100, decimal_places=3)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)

    cost = models.DecimalField(max_digits=100, decimal_places=3)

    size = models.DecimalField(max_digits=100, decimal_places=3)  # размер файлов игры

    description = models.TextField()  # неограниченное количество текста

    age_limited = models.BooleanField(default=False)

    buyer = models.ManyToManyField(Buyer)  # связь с моделью Buyer


Buyer.objects.create(name='otshelnik', balance=725, age=17)
Game.objects.create(title='GTA VI', cost=35, size=12.2, description='finally!', age_limited=True)
Game.objects.create(title='Tanki', cost=20, size=7.4, description='tank man!', age_limited=False)
Game.objects.create(title='CS GO II', cost=15, size=3.8, description='strike!', age_limited=False)
Game.objects.filter(title='CS GO II').update(age_limited=True)





