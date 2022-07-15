from django.db import models


class Vocation(models.Model):
    name = models.CharField(max_length=50, null=False)
    intellect_modifier = models.DecimalField(max_digits=10, decimal_places=2)
    strength_modifier = models.DecimalField(max_digits=10, decimal_places=2)
    agility_modifier = models.DecimalField(max_digits=10, decimal_places=2)
