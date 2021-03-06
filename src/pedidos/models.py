from django.db import models
from django.core.validators import MinValueValidator

# Modelo dos Clientes no banco de dados 
class Cliente(models.Model):
	nome 	= models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.nome

#Modelo de validação da classe produtos
class Produto(models.Model):
	nome 			= models.CharField(max_length=200, null=True)
	preço_unitario	= models.DecimalField(decimal_places=2, validators=[MinValueValidator(0.01)], null=True, max_digits=100)
	multiplo 		= models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1)])

	def __str__(self):
		return self.nome

#Modelo de validação da classe pedido

RENTABILIDADE = (
	('Ótima', 'Ótima'),
	('Boa', 'Boa'),
	('Ruim', 'Ruim'),)

class Pedido(models.Model):
	cliente 		= models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
	produto 		= models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
	quantidade		= models.PositiveIntegerField(null=True, validators=[MinValueValidator(1)])
	preço_item		= models.DecimalField(null=True, decimal_places=2, max_digits=100, validators=[MinValueValidator(0.01)])
	rentabilidade	= models.CharField(max_length=100, null=True, choices=RENTABILIDADE, blank=True)

	def __str__(self):
		return f'{self.cliente.nome} - {self.produto.nome}'



