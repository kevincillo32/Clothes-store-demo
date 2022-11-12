from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Home', views.index, name='index'),
    path('camisas', views.camisas, name='camisas'),
    path('gorras', views.gorras, name='gorras'),
    path('sudaderas',views.sudaderas, name='sudaderas'),
    path('zapatos', views.zapatos, name='zapatos'),
    path('mochilas', views.mochilas, name='mochilas'),
    path('balones', views.balones, name='balones'),
]