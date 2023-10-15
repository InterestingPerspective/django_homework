import json

from django.core.management import BaseCommand

from catalog.models import Category
from config.settings import BASE_DIR


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(BASE_DIR / 'data2.json') as file:
            category_list = json.load(file)

        categories_for_create = []
        for category in category_list:
            categories_for_create.append(Category(category['pk'], category['fields']['name']))

        Category.objects.bulk_create(categories_for_create)
