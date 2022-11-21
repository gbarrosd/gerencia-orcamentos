# Generated by Django 4.1.3 on 2022-11-21 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("gerencia", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Secretaria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255, verbose_name="Nome")),
                (
                    "cnpj",
                    models.CharField(
                        max_length=50, null=True, unique=True, verbose_name="CNPJ"
                    ),
                ),
            ],
            options={
                "verbose_name": "Secretaria",
                "verbose_name_plural": "Secretarias",
            },
        ),
        migrations.AddField(
            model_name="orcamento",
            name="valor",
            field=models.IntegerField(blank=True, null=True, verbose_name="Valor"),
        ),
        migrations.AddField(
            model_name="orcamento",
            name="secretaria",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="orcamentos",
                to="gerencia.secretaria",
                verbose_name="Secretaria",
            ),
        ),
    ]
