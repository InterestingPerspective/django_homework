# Generated by Django 4.2.4 on 2023-09-10 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='creation_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='change_date',
            new_name='updated_at',
        ),
    ]
