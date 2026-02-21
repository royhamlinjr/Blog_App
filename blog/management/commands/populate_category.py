from blog.models import Category
from django.core.management.base import BaseCommand
from typing import Any

class Command(BaseCommand):
    help="This command inserts category data"

    def handle(self, *args:Any, **options:Any):

        #delete existing data
        Category.objects.all().delete()

        categories = ['Sports','Technology','Arts','Science','Business']

        for category_name in categories:
            Category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("Completed Inserting Data!")) 