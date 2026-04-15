from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.PROTECT)
    name = models.CharField(verbose_name="Maxsulot nomi", max_length=50, unique=True)
    price = models.DecimalField(verbose_name="Maxsulot narxi", max_digits=12, decimal_places=2)
    image = models.ImageField(verbose_name="Maxsulot rasmi", upload_to="media/", null=True, blank=True)

    def __str__(self):
        return self.name
