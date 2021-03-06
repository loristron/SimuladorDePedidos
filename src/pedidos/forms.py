from django import forms
from .models import Item 

class PostModelForm(forms.Form):
	class Meta:
		model 	= Item
		fields 	= [
			'produto',
			'quantidade',
			'preço_item',
			'rentabilidade',
		]