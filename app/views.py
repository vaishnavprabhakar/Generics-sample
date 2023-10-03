from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CategorySerializer
from . models import Category
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import View

Category.objects.update


# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()

    serializer_class = CategorySerializer

    

    def create(self, request,format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            Category.objects.create(
                cate_name = serializer.validated_data.get('cate_name')

            )
            return Response({"MSG":"CREATED_201"},status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors)
    
    
    
    