# Generated by Django 4.2.6 on 2023-11-16 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_delete_stock_remove_product_sizes_orderitem_cancel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='cancel',
        ),
        migrations.AddField(
            model_name='order',
            name='cancel',
            field=models.BooleanField(default=False),
        ),
    ]
