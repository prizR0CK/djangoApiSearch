from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from scraping.views import SearchViewSet, GoodsViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Scraping",
        default_version='v1',
        description="API for scraping",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@swaggerBlog.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

Router = routers.DefaultRouter()
Router.register('search', SearchViewSet, basename='search')
Router.register('goods', GoodsViewSet, basename='goods')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(Router.urls)),
    path('doc', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
