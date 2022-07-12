from django.db import models


class Character(models.Model):
    username = models.CharField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=255)
    level = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    gold = models.IntegerField(default=0)

    account = models.ForeignKey(
        "accounts.Account",
        on_delete=models.DO_NOTHING,
        related_name="characters",
    )

    missions = models.ManyToManyField("missions.Missions", related_name="characters")
