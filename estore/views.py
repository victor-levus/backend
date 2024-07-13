from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAdminUser, IsAuthenticated

from estore.serializers import  CategorySerializer, ProductSerializer
from .models import Category, Product



# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def get_permissions(self):
    #     if self.request.method in SAFE_METHODS:
    #         return [AllowAny()]
    #     return [IsAdminUser()]

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def get_permissions(self):
    #     if self.request.method in SAFE_METHODS:
    #         return [AllowAny()]
    #     return [IsAdminUser()]