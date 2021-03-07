from django.db import models
from django.core.validators import MinValueValidator

import decimal

#====================================================================================
#=================== Modelo de validação da Cliente Pedido ==========================
#====================================================================================
#cliente 	 = campo obriagatório, seleciona um objeto do tipo Cliente
#items 		 = permite a inclusão de múltiplos objetos do tipo Item. Campo obrigatório
#total_items = campo prenchido pré ao salvamento na lógica descrita em signals.py
class Cliente(models.Model):
	nome 	= models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.nome

#====================================================================================
#=================== Modelo de validação da classe Produtos =========================
#====================================================================================
#
#
#

class Produto(models.Model):
	nome 			= models.CharField(max_length=200, null=True)
	preço_unitario	= models.DecimalField(decimal_places=2, validators=[MinValueValidator(0.01)], null=True, max_digits=100)
	multiplo 		= models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1)])

	def __str__(self):
		return self.nome

#====================================================================================
#=================== Modelo de validação da classe Item =============================
#====================================================================================
#
#
#
#
class Item(models.Model):
	produto 		= models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
	quantidade		= models.PositiveIntegerField(null=True, validators=[MinValueValidator(1)])
	preço_item		= models.DecimalField(null=True, decimal_places=2, max_digits=100, validators=[MinValueValidator(0.01)], blank=True)
	rentabilidade 	= models.CharField(null=True, blank=True, max_length=200)

	#nominação string dos objetos
	def __str__(self):
		return f'{self.produto.nome} - R${self.preço_item} - {self.rentabilidade}'


#====================================================================================
#=================== Modelo de validação da classe Pedido ===========================
#====================================================================================
#cliente 	 = campo obriagatório, seleciona um objeto do tipo Cliente
#items 		 = permite a inclusão de múltiplos objetos do tipo Item. Campo obrigatório
#total_items = campo prenchido pré ao salvamento na lógica descrita em signals.py

class Pedido(models.Model):
	cliente 		= models.ForeignKey(Cliente, on_delete=models.CASCADE)
	items 			= models.ManyToManyField(Item)
	total_price		= models.DecimalField(decimal_places=2, null=True, max_digits=1000, blank=True)
	total_items		= models.PositiveIntegerField(null=True, blank=True)
	pedido_validado	= models.BooleanField(null=True, blank=False, default=False)

	#nominação string dos objetos 
	def __str__(self):
		return f'{self.cliente.nome} - R${self.total_price}'