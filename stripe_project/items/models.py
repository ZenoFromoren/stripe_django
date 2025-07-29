from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()

    class Meta:
        db_table = "items"
        verbose_name = "item"
        verbose_name_plural = "items"

    def __str__(self):
        return self.name
