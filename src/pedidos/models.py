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
	quantidade		= models.PositiveIntegerField(null=True, validators=[MinValueValidator(1)])
	preço_unitario	= models.DecimalField(decimal_places=2, validators=[MinValueValidator(0.01)], null=True, max_digits=100)
	multiplo 		= models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1)])

	def __str__(self):
		return self.nome

