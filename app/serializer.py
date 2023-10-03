from rest_framework import serializers
from .models import Category
from rest_framework.validators import ValidationError


class CategorySerializer(serializers.Serializer):

    cate_name = serializers.CharField()


    def create(self, validated_data):
        cate_obj = Category.objects.create(
            cate_name = validated_data.get('category_name')
        )
        return validated_data
    

    def update(self, instance, validated_data):
        instance.category_name = validated_data.get('category_name', instance.category_name)
        instance.save()
        return instance

    