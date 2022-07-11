from django.db import models


class Missions(models.Model):
    description = models.TextField(null=False)
    name = models.CharField(max_length=50, null=False)
    experience = models.IntegerField(null=False)
    level_required = models.IntegerField()
    gold = models.IntegerField()
    xp = models.IntegerField()

    created_by = models.ForeignKey(
        "patrons.Patron", on_delete=models.CASCADE, related_name="missions"
    )
