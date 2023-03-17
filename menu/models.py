from django.db import models


class FoodCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название категории")
    is_publish = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название топпинга")

    def __str__(self):
        return self.name


class Food(models.Model):
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, verbose_name="Категория блюда" )
    name = models.CharField(max_length=50, null=False, verbose_name="Название блюда")
    description = models.TextField(null=True, blank=True, max_length=1000, verbose_name="Описание")
    price = models.IntegerField(null=True, blank=True, verbose_name="Стоимость")
    is_special = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_publish = models.BooleanField(default=True)
    toppings = models.ManyToManyField(Topping)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
