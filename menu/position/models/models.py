from django.db import models
from django.core import validators


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Allergen(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Allergen'
        verbose_name_plural = 'Allergens'

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField('name', max_length=255)
    image = models.ImageField('image', upload_to='positions/', blank=True, null=True)
    price = models.DecimalField('price', max_digits=10, decimal_places=2)
    proteins = models.PositiveSmallIntegerField("Proteins", validators=[validators.MaxValueValidator(10000)])
    fats = models.PositiveSmallIntegerField("Fats", validators=[validators.MaxValueValidator(10000)])
    carbohydrates = models.PositiveSmallIntegerField("Carbohydrates", validators=[validators.MaxValueValidator(10000)])
    calories = models.PositiveSmallIntegerField(verbose_name="Calories")
    allergens = models.ManyToManyField(Allergen, blank=True, related_name='product_allergens', verbose_name='Allergens')
    category = models.ForeignKey(Category, related_name='positions', on_delete=models.CASCADE,
                                 verbose_name='Categories')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

    def __str__(self):
        return self.name
