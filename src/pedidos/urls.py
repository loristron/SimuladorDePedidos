from django.urls import path
from .views import dashboard_view, update_pedido_view

app_name = 'pedidos'

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('update-pedido=<int:pk>', update_pedido_view, name='update-pedido'),
]
