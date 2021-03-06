from django import forms
from .models import Item, Pedido

class ItemModelForm(forms.Form):
	class Meta:
		model 	= Item
		fields 	= [
			'produto',
			'quantidade',
			'preço_item',
			'rentabilidade',
		]

class PedidoModelForm(forms.Form):
	class Meta:
		model 	= Pedido
		fields	= [
			'cliente',
			'items',
			'total_price',
		]