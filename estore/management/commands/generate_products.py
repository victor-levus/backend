import os
import random
from io import BytesIO
from PIL import Image
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.utils.text import slugify
from estore.models import Product, Category

class Command(BaseCommand):
    help = 'Generate random products'

    def handle(self, *args, **kwargs):
        categories = Category.objects.all()
        if not categories.exists():
            self.stdout.write(self.style.ERROR('No categories found. Please add some categories first.'))
            return

        product_data = [
            {
                'name': 'Wireless Mouse',
                'description': 'A sleek and modern wireless mouse with ergonomic design.',
                'sku': 'WM12345',
                'price': 29.99,
            },
            {
                'name': 'Mechanical Keyboard',
                'description': 'A high-quality mechanical keyboard with RGB lighting.',
                'sku': 'MK67890',
                'price': 89.99,
            },
            {
                'name': 'Noise Cancelling Headphones',
                'description': 'Over-ear headphones with active noise cancellation.',
                'sku': 'NC11223',
                'price': 199.99,
            },
            {
                'name': '4K Monitor',
                'description': 'A stunning 27-inch 4K monitor with HDR support.',
                'sku': '4K45678',
                'price': 349.99,
            },
            {
                'name': 'Gaming Chair',
                'description': 'An ergonomic gaming chair with lumbar support.',
                'sku': 'GC91011',
                'price': 149.99,
            }
        ]

        for data in product_data:
            category = random.choice(categories)

            product = Product(
                name=data['name'],
                description=data['description'],
                sku=data['sku'],
                price=data['price'],
                category=category
            )

        
                
            product.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created {data["name"]}'))
