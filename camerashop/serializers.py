from rest_framework import serializers
from camerashop.models import *


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        data = validated_data.copy()
        u = User(**data)
        u.set_password(u.password)
        u.save()
        return u

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['avatar'] = instance.avatar.url if instance.avatar else ''
        return data

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'last_name', 'first_name', 'avatar', 'email', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'username': {'required': True},
            'last_name': {'required': True}
        }


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'description']


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategories']


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductImageSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['image'] = instance.image.url if instance.image else ''
        return data

    class Meta:
        model = ProductImage
        fields = ['id', 'image']


class ProductSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    images = ProductImageSerializer(many=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['main_image'] = instance.main_image.url if instance.main_image else ''
        return data

    class Meta:
        model = Product
        fields = ['id', 'name', 'manufacturer', 'price', 'stock', 'main_image', 'images', 'sale', 'stars']
