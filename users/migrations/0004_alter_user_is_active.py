# Generated by Django 4.2.4 on 2023-10-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активация'),
        ),
    ]
