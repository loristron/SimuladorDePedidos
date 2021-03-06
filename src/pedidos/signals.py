from django.db.models.signals import pre_save, m2m_changed
from django.dispatch import receiver

from random import randint
import decimal

from .models import Item, Pedido

#Recebe sinal e antes de salvar objetos da classe Item, calcula um preço sugerido para o item e 
#de acordo com esse preço, ou com qualquer preço que seja altarado a partir daí, classifica a rentabilidade
#do item de acordo com as especificações do exercício. 
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
	
@receiver(m2m_changed, sender=Pedido.items.through)
def pre_save_preço_total_pedido(sender, instance, action, **kwargs):
	total_price = 0
	total_items = 0

	if action =='post_add' or action == 'post_remove':
		
		for item in instance.items.all():
			total_items 	+= 1 
			total_price 	+= item.preço_item 
		
		instance.total_price = total_price
		instance.total_items = total_items
		instance.save()

	