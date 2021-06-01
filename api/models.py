from django.db import models


class Food(models.Model):
    COMIDA = 'COMIDA'
    BEBIDA = 'BEBIDA'
    SOBREMESA = 'SOBREMESA'
    CARNE = 'CARNE'
    VEGANO = 'VEGANO'
    VEGETARIANO = 'VEGETARIANO'
    SALADA = 'SALADA'
    FRUTA = 'FRUTA'

    CATEGORIES_CHOICES = [
        (COMIDA, 'Comida'),
        (BEBIDA, 'Bebida'),
        (SOBREMESA, 'Sobremesa'),
        (CARNE, 'Carne'),
        (VEGANO, 'Vegano'),
        (VEGETARIANO, 'Vegetariano'),
        (SALADA, 'Salada'),
        (FRUTA, 'Fruta'),
    ]

    id = models.IntegerField(name='id', primary_key=True)
    title = models.CharField(name='title', max_length=100)
    category = models.CharField(name='category', max_length=50, choices=CATEGORIES_CHOICES, default=COMIDA)
    imageUrl = models.URLField(name='urlField', max_length=500)
    isVegeterian = models.BooleanField(name='isVegeterian')
    isVegan = models.BooleanField(name='isVegan')

    def __str__(self):
        return f'{self.title}, {self.category}'


class Meal(models.Model):
    ALMOCO = 'ALMOCO'
    JANTAR = 'JANTAR'
    CAFE = 'CAFE DA MANHA'

    TYPE_CHOICES = [
        (ALMOCO, 'ALMOCO'),
        (JANTAR, 'JANTAR'),
        (CAFE, 'CAFE DA MANHA'),
    ]

    id = models.IntegerField(name='id', primary_key=True)
    type = models.CharField(name='type', max_length=50, choices=TYPE_CHOICES)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    date = models.DateField(name='date')

    def __str__(self):
        return f'{self.type}, {self.food.name}'
