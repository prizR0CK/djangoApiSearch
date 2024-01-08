from django.contrib import admin
from .models import Client, Goods


class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "search_query"]
    search_fields = ['name']


class GoodsAdmin(admin.ModelAdmin):
    list_display = ["shop_name", "link", "name", "price", "client"]
    search_fields = ['name']


admin.site.register(Client, ClientAdmin)
admin.site.register(Goods, GoodsAdmin)
