# Generated by Django 4.0.6 on 2022-07-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vocations", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vocation",
            name="agility_modifier",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="vocation",
            name="intellect_modifier",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="vocation",
            name="strength_modifier",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
