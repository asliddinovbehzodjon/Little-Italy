from rest_framework import serializers 
from .models import *
class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class SubCategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True,read_only=True)
    class Meta:
        model = SubCategory
        fields = ['name','products','id']
class CategorySerializer(serializers.ModelSerializer):
    products =ProductSerializer(many=True,read_only=True)
    subcategory=SubCategorySerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = '__all__'
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields =  ['id','shopping','product_id','quantity','product_name']  
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True,read_only=True)
    class Meta:
        model  = Order
        fields = ['all_shopping','all_products','items']
 