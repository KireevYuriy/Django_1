from django.urls import path
from adminapp.views import category

app_name = 'adminapp'
urlpatterns = [
    path('categories/create/', category.category_create, name='category_create'),
    path('categories/read/', category.categories, name='categories'),
    path('categories/update/<int:pk>/', category.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', category.category_delete, name='category_delete'),
]
