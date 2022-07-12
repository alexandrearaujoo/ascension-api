# Generated by Django 4.0.6 on 2022-07-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Missions",
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
                ("description", models.TextField()),
                ("name", models.CharField(max_length=50)),
                ("experience", models.IntegerField()),
                ("level_required", models.IntegerField()),
                ("gold", models.IntegerField()),
                ("xp", models.IntegerField()),
            ],
        ),
    ]
