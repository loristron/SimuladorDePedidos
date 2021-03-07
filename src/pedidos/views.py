from django.shortcuts import render
from django.contrib import messages
from .models import Item, Cliente, Produto, Pedido
from .forms import ItemModelForm, PedidoModelForm

# Create your views here.
def dashboard_view(request):


	qs_pedidos 		= Pedido.objects.all()
	qs_items 		= Item.objects.all()

	template_name 	= 'dashboard.html'
	context 		= {
			'page_title': 'Home Page',

			#Contadores 
			'total_clientes': Cliente.objects.all().count(),
			'total_produtos': Produto.objects.all().count(),
			'total_itens'	: Item.objects.all().count(),
			'total_pedidos' : Pedido.objects.all().count(),

			#Querysets
			'queryset_pedidos': qs_pedidos,
			'queryset_items': qs_items,

	}
	return render(request, template_name, context)

def update_pedido_view(request, pk):

	pedido 			= Pedido.objects.get(pk=pk)
	form 			= PedidoModelForm(request.POST or None, instance=pedido)
	
	if request.method == 'POST':
		if form.is_valid():
			instance = form.save()
			if instance.pedido_validado == False:
				messages.warning(request, 'Itens com rentabilidade ruim não são aceitos no pedido. Tente novamente com um pedido válido.')
				form = PedidoModelForm(request.POST or None, instance=pedido)
			if instance.pedido_validado == True:
				messages.info(request, 'Atualizações Salvas')
				form.save()
				form = PedidoModelForm(request.POST or None, instance=pedido)

	template_name 	= 'update-pedido.html'
	context			= {	
		'page_title': 'Update pedido #'+ str(pk),
		'form'		: form, 

	}

	return render(request, template_name, context)
