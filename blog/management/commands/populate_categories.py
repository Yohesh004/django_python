from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help="this command inserts post data"

    def handle(self, *args: Any, **options: Any) :
        Category.objects.all().delete()

        categories=[
            'Sports','Tech',"scie",'Art','Food'
        ]

        for category_name in categories:
             Category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("COMPLETED INSERTING DATA"))
            
