# Generated by Django 4.2.6 on 2023-11-09 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_order_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock'), ('Low Stock', 'Low Stock')], max_length=15)),
            ],
        ),
    ]
