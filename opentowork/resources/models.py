from django.db import models
from django.core.validators import MinValueValidator

class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='categories')
    

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name

class Resource(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]  # Asegura que el precio sea positivo
    )
    stock_quantity = models.PositiveIntegerField()
    is_featured = models.BooleanField(default=False)
    is_sponsored = models.BooleanField(default=False)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    subcategories = models.ManyToManyField('Subcategory', related_name='resources')
    image = models.ImageField(upload_to='resources/images/', blank=True, null=True)  # Campo de imagen

    def __str__(self):
        return self.name
