from django.db import models
from items.models import Item
from itertools import chain


class Order(models.Model):
    items = models.ManyToManyField(Item)
    created_at = models.DateField(auto_now_add=True)

    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = f.value_from_object(instance)
        for f in opts.many_to_many:
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data

    class Meta:
        db_table = "orders"
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
        return f"Заказ {self.id}"
