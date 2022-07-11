# Generated by Django 4.0.6 on 2022-07-11 15:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("artisans", "0001_initial"),
        ("characters", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("SW", "Sword"),
                            ("BOW", "Bow"),
                            ("SH", "Shield"),
                            ("AXE", "Axe"),
                            ("AR", "Armor"),
                            ("LE", "Legs"),
                        ],
                        max_length=50,
                    ),
                ),
                ("price", models.IntegerField()),
                ("level_requires", models.IntegerField(default=0)),
                (
                    "artisan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="items",
                        to="artisans.artisan",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="items",
                        to="characters.character",
                    ),
                ),
            ],
        ),
    ]
