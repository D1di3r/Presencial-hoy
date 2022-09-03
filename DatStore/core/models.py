
from statistics import mode
from tabnanny import verbose
from unicodedata import category, name
from django.db import models

class  Marca (models.Model):
    name=models.CharField(max_length=30,verbose_name="Nombre de la marca")
  
    def __str__(self):
        return self.name


    class Meta :
     verbose_name='Marca'
     db_table='marca'
     ordering= ['id']

class Category (models.Model):
   name=models.CharField(max_length=30,verbose_name="Nombre de la categoria")
   
   def __str__(self):
      return self.name

   class Meta :
     verbose_name='Categoria'
     verbose_name_plural='Categorias'
     db_table='categoria'
     ordering= ['id']

class Product (models.Model):
     name=models.CharField(max_length=40,verbose_name="Nombre del producto")
     description=models.TextField(verbose_name="Descripccion del producto")
     price=models.IntegerField(verbose_name="Precio del producto")
     category=models.ForeignKey(Category, on_delete=models.CASCADE)
# Create your models here.
