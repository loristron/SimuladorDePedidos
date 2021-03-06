from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from random import randint
import decimal

from .models import Produto, Item, Cliente

@receiver(pre_save, sender=Item)
def pre_save_preço_sugerido(sender, instance, **kwargs):
	
	if instance.preço_item == None:
		sugestao 	= randint(1, 1000000) / 100 * instance.quantidade
		instance.preço_item = sugestao

	if instance.preço_item > instance.produto.preço_unitario:
		instance.rentabilidade = 'Ótima'
		
	if instance.preço_item >= (
		instance.produto.preço_unitario - decimal.Decimal((float(instance.produto.preço_unitario) * 0.1))) and instance.preço_item < instance.produto.preço_unitario:
		instance.rentabilidade = 'Boa'
		
	if instance.preço_item <= instance.produto.preço_unitario - decimal.Decimal((float(instance.produto.preço_unitario) * 0.1)):
		 instance.rentabilidade = 'Ruim'
	


	