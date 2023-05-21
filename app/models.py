from django.db import models


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
        verbose_name='Описание'
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
