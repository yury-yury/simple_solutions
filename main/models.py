from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Name')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name
