# Generated by Django 2.2.2 on 2019-06-27 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_portfolio', '0012_remove_stock_initial_quant'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='stock_currency',
            field=models.CharField(default='SFFf', max_length=10),
            preserve_default=False,
        ),
    ]
