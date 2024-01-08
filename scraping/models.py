from django.db import models


class Client(models.Model):
    name = models.CharField("Name", max_length=300, unique=False)
    search_query = models.CharField("Search", max_length=500, unique=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ('name',)


class Goods(models.Model):
    shop_name = models.CharField("Shop Name", max_length=300, unique=False)
    link = models.CharField("Link", max_length=300, unique=False)
    name = models.CharField("Name", max_length=300, unique=False)
    price = models.CharField("Price", max_length=20, unique=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='goods')

    def __str__(self):
        return f"{self.shop_name} - {self.link} - {self.name} - {self.price} - {self.client}"

    class Meta:
        verbose_name = 'Good'
        verbose_name_plural = 'Goods'
        ordering = ('client',)
