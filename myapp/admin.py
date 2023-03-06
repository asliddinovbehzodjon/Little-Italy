from django.contrib import admin
from import_export.admin import ImportExportModelAdmin,ExportMixin
# Register your models here.
from modeltranslation.admin import TranslationAdmin
from .resources import * 
from .models import *
@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ['name','telegram_id','language','phone']
    search_fields = ['name','telegram_id','language','phone']
    list_filter = ['language','added']
    list_per_page = 10
@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 10
    resource_classes = [CategoryResource]
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','category']
    search_fields = ['name','category__name']
    list_per_page = 10
@admin.register(Product)
class ProducAdmin(ImportExportModelAdmin):
    list_display = ['picture','name','category','subcategory','price','discount']
    search_fields = ['name','category__name','subcategory__name']
    list_filter = ['discount','category','subcategory']
    list_per_page = 10
    resource_classes = [ProductResouces]
admin.site.register([Order,OrderItem])