from django.db import models
import uuid


class TypeChoices(models.TextChoices):
    SWORD = ("SW", "Sword")
    BOW = ("BOW", "Bow")
    SHIELD = ("SH", "Shield")
    AXE = ("AXE", "Axe")
    ARMOR = ("AR", "Armor")
    LEGS = ("LE", "Legs")


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TypeChoices.choices)
    price = models.IntegerField()
    level_required = models.IntegerField(default=0)
    artisan = models.ForeignKey(
        "artisans.Artisan",
        on_delete=models.SET_NULL,
        related_name="items",
        null=True,
    )
    owner = models.ForeignKey(
        "characters.Character",
        on_delete=models.SET_NULL,
        related_name="items",
        null=True,
    )

    def __str__(self):
        return self.name
