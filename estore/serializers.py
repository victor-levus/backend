from rest_framework import serializers
from estore.models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'sku', 'name', 'description', 'category', 'price', 'image', 'createdAt',
                  'updatedAt']
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image', 'createdAt',
                  'updatedAt']
        

    