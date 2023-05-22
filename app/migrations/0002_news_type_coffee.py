# Generated by Django 4.2.1 on 2023-05-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='type_coffee',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Зеленый кофе'), (2, 'Обжаренный кофе')], default=1, verbose_name='Тип кофе'),
            preserve_default=False,
        ),
    ]
