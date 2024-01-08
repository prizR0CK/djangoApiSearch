from .models import Client, Goods


def write_goods_list(name, search_query, goods_list):
    client = Client.objects.create(name=name, search_query=search_query)
    for key, value in goods_list.items():
        try:
            Goods.objects.create(shop_name=value[0], link=value[1], name=value[2], price=value[3], client=client)
        except Exception as err:
            print(err)
    return client.id
