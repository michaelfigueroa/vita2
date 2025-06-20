from django.db import models

# Create your models here.

class Property(models.Model):
    type = models.CharField(
        verbose_name='Tipo',
        max_length=12,
        default=''
    )
    business= models.CharField(
        verbose_name='Negocio',
        max_length=12,
        default=''
    )
    model = models.CharField(
        verbose_name='Modelo',
        max_length=12,
        default=''
    )
    orientation = models.CharField(
        verbose_name='Orientación',
        max_length=12,
        default=''
    )
    dimension = models.FloatField(
        verbose_name='Metraje útil',
        max_length=12,
        default=0
    )
    dimension_total = models.FloatField(
        verbose_name='Metraje total',
        max_length=5,
        default=0
    )
    status = models.CharField(
        verbose_name='Estado',
        max_length=5,
        default=''
    )
    washing = models.CharField(
        verbose_name='Lavadora',
        max_length=12,
        default='Si'
    )
    number= models.IntegerField(
        verbose_name='Número',
        default=1
    )
    floor = models.IntegerField(
        verbose_name='Piso',
        default=1
    )
    
    def __str__(self):
        return self.type+" N° "+str(self.number)