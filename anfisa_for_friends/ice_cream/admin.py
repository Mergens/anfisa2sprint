from django.contrib import admin

# Register your models here.
from .models import Category, IceCream, Topping, Wrapper
admin.site.empty_value_display = 'Не задано'


class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )    
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
        'slug',
        'output_order',
    )    
    list_editable = (
        'slug',
    )    
    list_display_links = ('title',)


class ToppingAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
    )
    list_editable = (
        'slug',
    )    
    list_display_links = ('title',)


class WrapperAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    list_display_links = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(Wrapper)
