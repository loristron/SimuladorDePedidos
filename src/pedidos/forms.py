from django import forms
from .models import Item, Pedido

class ItemModelForm(forms.ModelForm):
	class Meta:
		model 	= Item
		fields 	= [
			'produto',
			'quantidade',
			'preço_item',
			'rentabilidade',
		]

class PedidoModelForm(forms.ModelForm):
	class Meta:
		model 	= Pedido
		fields	= [
			'cliente',
			'items',
			'total_price',
		]

		labels = {
		'items': 'Itens do pedido',
		'total_price': 'Preço Total - Calculado Automaticamente',

		}

		widgets = {
		'total_price': forms.TextInput(attrs={'readonly': 'readonly'})
		}

