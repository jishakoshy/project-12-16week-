# Generated by Django 4.2.6 on 2023-11-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.IntegerField(blank=True, choices=[(7, '7'), (8, '8'), (9, '9')], default=None, null=True),
        ),
    ]
