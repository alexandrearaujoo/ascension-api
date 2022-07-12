from django.db import models
from django.contrib.auth.models import AbstractUser

from .utils import CustomUserManager


class ClassificationChoices(models.TextChoices):
    ANGEL = ("angel",)
    DEMON = ("demon",)


# Create your models here.
class Account(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    classification = models.CharField(
        max_length=50,
        choices=ClassificationChoices.choices,
        default=ClassificationChoices.ANGEL,
    )
    is_game_master = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["classification"]

    objects = CustomUserManager()
