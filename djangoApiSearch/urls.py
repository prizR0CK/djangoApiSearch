from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from scraping.views import SearchViewSet, GoodsViewSet

Router = routers.DefaultRouter()
Router.register('search', SearchViewSet, basename='search')
Router.register('goods', GoodsViewSet, basename='goods')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(Router.urls))
]
