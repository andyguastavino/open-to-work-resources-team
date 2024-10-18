

from django.urls import path
from .views import (
    resource_list, resource_detail, resource_create,resource_edit,resource_delete,
    category_list, category_create, category_edit, category_delete,
    subcategory_list, subcategory_create, subcategory_edit, subcategory_delete,
    section_list, section_create, section_edit, section_delete
)

urlpatterns = [
    path('', resource_list, name='resource_list'),
    path('create/', resource_create, name='resource_create'),
    path('edit/<int:pk>/', resource_edit, name='resource_edit'),
    path('detail/<int:resource_id>/', resource_detail, name='resource_detail'),
    path('delete/<int:pk>/', resource_delete, name='resource_delete'),
    path('categories/', category_list, name='category_list'),
    path('categories/create/', category_create, name='category_create'),
    path('categories/edit/<int:pk>/', category_edit, name='category_edit'),
    path('categories/delete/<int:pk>/', category_delete, name='category_delete'),
    path('subcategories/', subcategory_list, name='subcategory_list'),
    path('subcategories/create/', subcategory_create, name='subcategory_create'),
    path('subcategories/edit/<int:pk>/', subcategory_edit, name='subcategory_edit'),
    path('subcategories/delete/<int:pk>/', subcategory_delete, name='subcategory_delete'),
    path('sections/', section_list, name='section_list'),
    path('sections/create/', section_create, name='section_create'),
    path('sections/edit/<int:pk>/', section_edit, name='section_edit'),
    path('sections/delete/<int:pk>/', section_delete, name='section_delete'),
]
