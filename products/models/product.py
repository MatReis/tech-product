from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    provider = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
