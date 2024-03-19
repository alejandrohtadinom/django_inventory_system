from django.db import models

from product.models import Product
from supplier.models import Supplier
from warehouse.models import Warehouse


# Main item model
class Inventory(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    location = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    qtty = models.DecimalField(max_digits=12, decimal_places=2)
