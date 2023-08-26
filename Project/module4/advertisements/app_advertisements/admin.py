from django.contrib import admin
from .models import Advertisement
from django.utils.html import format_html
# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_at', 'user', 'auction', 'created_date', 'image']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)
    
    @admin.display(description='Image')
    def display_image(self, instance):
        if instance.image:
            return format_html('<img src="{}" height="100px" />', instance.image.url)
        else:
            return format_html('<img src="/static/img/adv.png" height="100px" />')

    list_display = ['title', 'display_image', 'created_at']

    
        
    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)
        
    fieldsets = (
        ('Общее', {
            'fields':('title', 'description', 'user', 'image'),
        }),
        ('Финансы', {
            'fields':('price', 'auction'),
            'classes': ['collapse']
        })
    )
        
admin.site.register(Advertisement, AdvertisementAdmin)
