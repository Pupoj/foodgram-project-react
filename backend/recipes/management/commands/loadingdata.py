import json
import os
from pathlib import Path

from django.core.management.base import BaseCommand
from recipes.models import Ingredient

BASE_DIR = Path(__file__).resolve().parent.parent


class Command(BaseCommand):

    def handle(self, *args, **options):
        file_name = 'ingredients.json'
        json_path = os.path.join(BASE_DIR, 'data')
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
            print(f'Файл {file_name} не найден.')
            return
