# Generated by Django 2.2.2 on 2019-06-26 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_portfolio', '0003_stock_initial_quant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='initial_quant',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]