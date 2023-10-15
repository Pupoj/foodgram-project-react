import json
import os

from django.core.management.base import BaseCommand
from foodgram.settings import DATA_DIR
from recipes.models import Ingredient


class Command(BaseCommand):

    def handle(self, *args, **options):
        json_path = os.path.join(DATA_DIR, 'ingredients.json')
        try:
            with open(json_path, 'rb') as file:
                data = json.load(file)
                ingredients = [
                    Ingredient(
                        name=item.get('name'),
                        measurement_unit=item.get('measurement_unit'),
                    )
                    for item in data
                ]
                Ingredient.objects.bulk_create(ingredients)
            print('finished')
        except FileNotFoundError:
            print('Файл не найден.')
            return
