from django.urls import path
from . import views

app_name = "mainapp"
urlpatterns = [
    path('', views.products, name='index'),
    path('category/<int:pk>/', views.products, name='category'),
    path('category/<int:pk>/page/<int:page>/', views.products, name='page'),
    path('products/<int:pk>/', views.products, name='products'),
]