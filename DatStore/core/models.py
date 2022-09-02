
from statistics import mode
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
     db_table='categoria'
     ordering= ['id']



# Create your models here.
