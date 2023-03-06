from .models import *
from modeltranslation.translator import TranslationOptions,register
@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'about',)
@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
