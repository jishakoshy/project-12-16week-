# Generated by Django 4.2.6 on 2023-11-25 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_product_quantity_product_size_delete_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_varient',
            field=models.BooleanField(default=False),
        ),
    ]
