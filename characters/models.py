from django.db import models


class Character(models.Model):
    username = models.CharField(max_length=50, unique=True, null=False)
    password = models.CharField()
    level = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    gold = models.IntegerField(default=0)

    patron = models.ForeignKey(
        "patrons.Patron", on_delete=models.DO_NOTHING, related_name="characters"
    )
