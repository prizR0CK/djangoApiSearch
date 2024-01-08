from rest_framework import viewsets
from .serializers import SearchClientSerializer, GoodsSerializer
from .models import Client, Goods

client_id = 0


class SearchViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.order_by('-id')[:1]
    serializer_class = SearchClientSerializer


class GoodsViewSet(viewsets.ModelViewSet):
    serializer_class = GoodsSerializer

    def get_queryset(self):
        global client_id
        return Goods.objects.select_related('client').filter(client=client_id)
