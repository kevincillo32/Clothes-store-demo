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
    path('camisagris', views.camisagris, name='camisagris'),
    path('camisablanca', views.camisablanca, name='camisablanca'),
    path('camisablanca2', views.camisablanca2, name='camisablanca2'),
    path('camisanegra', views.camisanegra, name='camisanegra'),
    path('camisaazul', views.camisaazul, name='camisaazul'),
    path('camisaroja', views.camisaroja, name='camisaroja'),
]
