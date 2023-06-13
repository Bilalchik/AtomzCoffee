from django.db import models


class TypeCoffeeChoice(models.TextChoices):
    GREEN_COFFEE = "1", "Зеленый кофе"
    FRIED_COFFEE = "2", "Обжаренный кофе"


class Currency(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название валюты'
    )
    short_name = models.CharField(
        max_length=50,
        verbose_name='Краткое название валюты'
    )
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'


class Treatment(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Тип кофе (мытый, сухой и т.д.)'
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Тип кофе'
        verbose_name_plural = 'Типы кофе'
    

class News(models.Model):
    image = models.ImageField(
        upload_to='media/images',
        verbose_name='Фотография'
    )
    header = models.CharField(
        max_length=225,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание в виде json'
    )
    type_coffee = models.CharField(
        max_length=3,
        choices=TypeCoffeeChoice.choices,
        verbose_name='Тип кофе',
        unique=True
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_date = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class CoffeeDescription(models.Model):
    coffee = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        verbose_name='Кофе',
        related_name='descriptions'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Сорт (название) коффе'
    )
    size = models.CharField(
        max_length=255,
        verbose_name='Размер пачки',
        blank=True
    )
    grade = models.CharField(
        max_length=255,
        verbose_name='Оценка',
        blank=True,
        default=''
    )
    treatment = models.ForeignKey(
        Treatment,
        on_delete=models.PROTECT,
        related_name='coffee_desc',
        verbose_name='Тип',
        blank=True,
        null=True
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0,
        verbose_name='Цена'
    )
    currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        verbose_name='Валюта'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описании'
