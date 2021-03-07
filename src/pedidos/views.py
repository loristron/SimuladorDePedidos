from django.shortcuts import render

from .models import Item, Cliente, Produto, Pedido
from .forms import ItemModelForm

# Create your views here.
def dashboard_view(request):

	qs_pedidos 		= Pedido.objects.all()
	qs_items 		= Item.objects.all()

	template_name 	= 'dashboard.html'
	context 		= {
			'page_title': 'Home Page',
			'total_clientes': Cliente.objects.all().count(),
			'total_produtos': Produto.objects.all().count(),
			'total_itens'	: Item.objects.all().count(),
			'total_pedidos' : Pedido.objects.all().count(),
			'queryset_pedidos': qs_pedidos,
			'queryset_items': qs_items,
	}
	return render(request, template_name, context)