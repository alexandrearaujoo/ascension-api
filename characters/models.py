from django.db import models


class Character(models.Model):

    username = models.CharField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=255)
    level = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    gold = models.IntegerField(default=0)
    health_points = models.IntegerField(default=100)

    strength = models.IntegerField(default=10)
    intellect = models.IntegerField(default=10)
    agility = models.IntegerField(default=10)

    vocation = models.ForeignKey(
        "vocations.Vocation",
        on_delete=models.CASCADE,
        related_name="characters",
    )

    account = models.ForeignKey(
        "accounts.Account",
        on_delete=models.DO_NOTHING,
        related_name="characters",
    )

    missions = models.ManyToManyField(
        "missions.Missions", related_name="characters"
    )
