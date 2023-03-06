from import_export.resources import ModelResource
from .models import *
class CategoryResource(ModelResource):
    class Meta:
        model=Category
class ProductResouces(ModelResource):
    class Meta:
        model = Product
        