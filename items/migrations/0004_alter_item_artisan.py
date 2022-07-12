# Generated by Django 4.0.6 on 2022-07-12 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("artisans", "0001_initial"),
        ("items", "0003_alter_item_artisan"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="artisan",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="items",
                to="artisans.artisan",
            ),
        ),
    ]