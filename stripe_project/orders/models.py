from django.db import models
from stripe_project.items.models import Item


class Order(models.Model):
    items = models.ManyToManyField(Item)
