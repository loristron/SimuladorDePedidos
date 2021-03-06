from django.db import models
from django.core.validators import MinValueValidator
# Modelo dos Clientes no banco de dados 
class Cliente(models.Model):
	nome 	= models.CharField(max_length=200, null=True)

class Produto(models.Model):
	nome 			= models.CharField(max_length=200, null=True)
	cliente 		= models.ForeignKey(Cliente)
	quantidade		= models.IntegerField
	preço_unitario	= models.DecimalField(decimal_places=2, validators=[MinValueValidator(0.01)], null=True, max_digits=100)
	multiplo 		= models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1)])
