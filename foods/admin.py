from django.contrib import admin
from .models import Category, Foods
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    exclude = ['slug']
class FoodsAdmin(admin.ModelAdmin):
    exclude = ['created_dt', 'update_dt']
admin.site.register(Category,CategoryAdmin)
admin.site.register(Foods,FoodsAdmin)