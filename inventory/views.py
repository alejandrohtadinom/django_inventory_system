from rest_framework import permissions, viewsets
from product.models import Product, Category
from warehouse.models import Warehouse, Location
from supplier.models import Supplier

from inventory.serializers import (
    ProductSerializer,
    CategorySerializer,
    WarehouseSerializer,
    LocationSerializer,
    SupplierSerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("title")
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("title")
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all().order_by("title")
    serializer_class = WarehouseSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by("title")
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by("company_name")
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated]
