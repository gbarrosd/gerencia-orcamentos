# Generated by Django 4.1.3 on 2022-11-21 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gerencia", "0003_alter_secretaria_cnpj"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orcamento",
            name="valor",
            field=models.FloatField(blank=True, null=True, verbose_name="Valor"),
        ),
    ]
