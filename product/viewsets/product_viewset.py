
from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers.product_serializer import ProductSerializer

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self): # via método get, poderia ser também queryset = Product.objects.all() 
        return Product.objects.all()
