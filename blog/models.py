from django.db import models


NULLABLE = {'null': True, 'blank': True}


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    body = models.TextField(verbose_name='содержимое')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    preview_img = models.ImageField(upload_to='blog_images/', verbose_name='изображение', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
