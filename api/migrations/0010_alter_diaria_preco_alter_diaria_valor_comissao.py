# Generated by Django 5.0.6 on 2024-08-06 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_diaria_candidatos_diaria_candidatas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaria',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='diaria',
            name='valor_comissao',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
