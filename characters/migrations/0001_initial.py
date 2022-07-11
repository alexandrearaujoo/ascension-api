# Generated by Django 4.0.6 on 2022-07-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Character",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=50, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("level", models.IntegerField(default=0)),
                ("experience", models.IntegerField(default=0)),
                ("gold", models.IntegerField(default=0)),
            ],
        ),
    ]
