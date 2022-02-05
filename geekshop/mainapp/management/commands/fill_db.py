from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser
import json, os

JSON_PATH = "mainapp/json"


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + ".json"), "r") as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json("categories")

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category, _ = ProductCategory.objects.get_or_create(**category)
            new_category.save()
        products = load_from_json("products")
        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            _category = ProductCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            product["category"] = _category
            new_product, _ = Product.objects.get_or_create(product['name'])
            for field, value in product:
                setattr(new_product, field, value)
            new_product.save()
        # Создаем суперпользователя при помощи менеджера модели
        super_user = ShopUser.objects.create_superuser(
            "django", "django@geekshop.local", "geekbrains"
        )
