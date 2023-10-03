from django.urls import path
from app.views import  CategoryViewSet




urlpatterns = [
    path('user/', 
         CategoryViewSet.as_view( 
             {'get':'list',
              'post':'create',
              'delete':'destroy'})
        )
    
    
]

