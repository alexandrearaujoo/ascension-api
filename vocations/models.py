from django.db import models


class Vocation(models.Model):
    name = models.CharField(max_length=50, null=False)
    intellect_modifier = models.DecimalField(decimal_places=2, max_digits=3)
    strength_modifier = models.DecimalField(decimal_places=2, max_digits=3)
    agility_modifier = models.DecimalField(decimal_places=2, max_digits=3)
