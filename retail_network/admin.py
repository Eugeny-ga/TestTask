from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from retail_network.models import Contacts, Product, Factory, Entrepreneur, Retailer

admin.site.register(Product)
admin.site.register(Contacts)


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'contacts', 'arrears']

    list_filter = ['contacts__city']
    actions = ['clear_arrears']

    def clear_arrears(self, request, queryset):
        queryset.update(arrears=0)
        self.message_user(request, 'Arrears cleared successfully.')

    clear_arrears.short_description = 'Обнулить задолженность'


@admin.register(Entrepreneur)
class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('title', 'contacts', 'provider_link', 'arrears')
    list_filter = ['contacts__city']
    actions = ['clear_arrears']

    def provider_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:retail_network_retailer_change", args=(obj.provider.pk,)),
            obj.provider.title
        ))

    provider_link.allow_tags = True
    provider_link.admin_order_field = 'Поставщик'
    provider_link.short_description = 'Поставщик'

    def clear_arrears(self, request, queryset):
        queryset.update(arrears=0)
        self.message_user(request, 'Arrears cleared successfully.')

    clear_arrears.short_description = 'Обнулить задолженность'


@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ('title', 'contacts', 'provider_link', 'arrears')
    list_filter = ['contacts__city']
    actions = ['clear_arrears']

    def provider_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:retail_network_factory_change", args=(obj.provider.pk,)),
            obj.provider.title
        ))

    provider_link.allow_tags = True
    provider_link.admin_order_field = 'Поставщик'
    provider_link.short_description = 'Поставщик'

    @admin.action
    def clear_arrears(self, request, queryset):
        queryset.update(arrears=0)
        self.message_user(request, 'Arrears cleared successfully.')

    clear_arrears.short_description = 'Обнулить задолженность'
