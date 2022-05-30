from django.contrib import admin
from .models import Position, Category, Allergen


class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_editable = ('category',)
    ordering = ('name',)
    sortable_by = ('name', 'price')
    list_filter = ('category',)
    list_per_page = 3
    filter_horizontal = ('allergens',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AllergenAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Position, PositionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Allergen, AllergenAdmin)
