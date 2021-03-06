from django.apps import AppConfig


class PedidosConfig(AppConfig):
    name = 'pedidos'

    def ready(self):
    	import pedidos.signals
    	
