from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.utils.html import format_html
# Create your models here.
class BotUser(models.Model):
    name  = models.CharField(max_length=150,null=True,blank=True,verbose_name="Name",help_text="Enter name")
    telegram_id = models.CharField(max_length=20,unique=True,verbose_name="Telegram ID")
    language  = models.CharField(max_length=5,default='uz',verbose_name="Language")
    phone  = models.CharField(max_length=20,null=True,blank=True,verbose_name="Phone Number")
    added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table= 'BotUser'
        verbose_name = "BotUser"
        verbose_name_plural = "BotUsers"
class Category(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True,verbose_name="Category")
    def __str__(self):
        return self.name
    class Meta:
        db_table= 'Category'
        verbose_name = "Category"
        verbose_name_plural = "Categories"
class SubCategory(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True,verbose_name="SubCategory")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Category")
    def __str__(self):
        return self.name
    class Meta:
        db_table= 'SubCategory'
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"
class Product(models.Model):
    name =models.CharField(max_length=150,verbose_name="Name")
    category =models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    subcategory = ChainedForeignKey(SubCategory,chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True)
    image = models.ImageField(upload_to='product-images',verbose_name="Image",null=True,blank=True)
    about = models.TextField(null=True,blank=True,verbose_name="Info")
    price  = models.IntegerField(null=True,blank=True)
    discount = models.IntegerField(verbose_name="Discount",null=True,blank=True)
    @property
    def picture(self):
        return format_html('<img src="{}" width="50" height="50" style="border-radius:50%" />'.format(self.image.url))
class Order(models.Model):
    user = models.ForeignKey(BotUser,on_delete=models.CASCADE,verbose_name="User")
    def __str__(self):
        if self.user.name:
            return self.user.name
        else:
            return f"User with ID: {self.user.telegram_id}"
    @property
    def all_shoping(self):
        items = self.items.all()
        total = sum([item.shopping for item in items])
        return total
    @property
    def all_products(self):
        items = self.items.all()
        total = sum([item.quantity for item in items])
        return total
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="Product")
    quantity = models.IntegerField(verbose_name="Quantity",default=1)
    def __str__(self) -> str:
        return self.order
    @property
    def shopping(self):
        if self.product.discount:
           return (self.product.price - self.product.discount) * self.quantity
        else:
            return (self.product.price) * self.quantity
    