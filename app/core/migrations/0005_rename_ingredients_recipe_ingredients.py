# Generated by Django 3.2.25 on 2025-01-07 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_auto_20250107_0513"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recipe",
            old_name="Ingredients",
            new_name="ingredients",
        ),
    ]
