from django.db import models


class Vocation(models.Model):
    name = models.CharField(max_length=50, null=False)
    intellect_modifier = models.DecimalField()
    strength_modifier = models.DecimalField()
    agility_modifier = models.DecimalField()
