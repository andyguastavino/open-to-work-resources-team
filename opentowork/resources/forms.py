# forms.py
from django import forms
from .models import Resource, Section, Category, Subcategory



class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['sku', 'name', 'description', 'price', 'stock_quantity', 'is_featured', 'is_sponsored', 'section', 'category', 'subcategories', 'image']

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'section']

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']
