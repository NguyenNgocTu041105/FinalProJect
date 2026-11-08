from django.contrib.auth.hashers import identify_hasher
from rest_framework import serializers
from .models import Product,Category,Brand

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    id_category=CategorySerializer(read_only=True)
    id_brand=BrandSerializer(read_only=True)
    class Meta:
        model=Product
        fields='__all__'