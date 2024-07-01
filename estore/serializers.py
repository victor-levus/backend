from rest_framework import serializers
from estore.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image', 'createdAt',
                  'updatedAt']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'sku', 'name', 'description', 'category', 'price', 'image', 'createdAt',
                  'updatedAt']
        

        

    