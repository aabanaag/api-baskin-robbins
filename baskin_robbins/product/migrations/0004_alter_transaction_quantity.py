# Generated by Django 4.1.3 on 2022-11-30 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_alter_recipe_product_alter_recipeingredient_recipe_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="quantity",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
