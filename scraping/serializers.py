from rest_framework import serializers
from .models import Client, Goods


class SearchClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['name', 'search_query']


class GoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goods
        fields = ['shop_name', 'link', 'name', 'price']
        read_only_fields = ['shop_name', 'link', 'name', 'price']
