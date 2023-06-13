from typing import Any
from random import randint
from django.contrib import admin
from .models import News, CoffeeDescription, Currency, Treatment, TypeCoffeeChoice


class CoffeeDescriptionInline(admin.TabularInline):
    
    model = CoffeeDescription


class NewsAdmin(admin.ModelAdmin):
    list_display = ['header', 'type_coffee', 'image', 'updated_date']
    list_filter = ['type_coffee', 'updated_date']
    search_fields = ['header', 'description']
    exclude = ['description']
    inlines = [CoffeeDescriptionInline]
    
    def save_related(self, request, form, formsets, change):
        form.save_m2m()
        for formset in formsets:
            self.save_formset(request, form, formset, change=change)
            
        descriptions = []
        
        if form.instance.type_coffee == TypeCoffeeChoice.GREEN_COFFEE:
            for description in form.instance.descriptions.all():
                descriptions.append(
                    {
                        "key": description.id if description.id is not None else randint(1, 10000),
                        "name": description.name,
                        "size": description.size,
                        "treatment": description.treatment.name,
                        "price": f'{description.price} {description.currency.short_name}',
                        "description": description.description
                    }
                )
        elif form.instance.type_coffee == TypeCoffeeChoice.FRIED_COFFEE:
            for description in form.instance.descriptions.all():
                descriptions.append(
                    {
                        "key": description.id if description.id is not None else randint(1, 10000),
                        "sort": description.name,
                        "grade": description.grade,
                        "price": f'{description.price} {description.currency.short_name}',
                        "description": description.description
                    }
                )
        
        form.instance.description_text = str(descriptions)
        form.instance.save()

    
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name']
    search_fields = ['name', 'short_name']
    
    
admin.site.register(News, NewsAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Treatment)
