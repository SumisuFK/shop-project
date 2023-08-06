from django.contrib import admin
from .models import Product, ProductImage
from django.utils.safestring import mark_safe

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','get_image', 'price', 'preorder']
    list_editable = ['price']
    inlines = [ProductImageInline]
    
    def get_image(self, obj):
        if obj.images.first():
            return mark_safe("<img src='{}' width='60' />".format(obj.images.first().image.url))
        return "None"
    
    get_image.short_desctiption = 'Фото'
    