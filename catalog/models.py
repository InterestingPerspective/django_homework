from django.conf import settings
from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    preview_img = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

        permissions = [
            (
                'set_published',
                'Can publish posts'
            ),
            (
                'set_category',
                'Can change category'
            ),
            (
                'set_description',
                'Can change description'
            ),
        ]


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='номер')
    name = models.CharField(max_length=100, verbose_name='название')
    is_active = models.BooleanField(verbose_name='признак')

    def __str__(self):
        return f'{self.number} - {self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
