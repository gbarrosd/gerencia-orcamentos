# Generated by Django 4.1.3 on 2022-11-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Orcamento",
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
                (
                    "numero",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="número do orçamento",
                    ),
                ),
                (
                    "criado_em",
                    models.DateTimeField(auto_now_add=True, verbose_name="criado em"),
                ),
                (
                    "atualizado_em",
                    models.DateTimeField(auto_now=True, verbose_name="atualizado em"),
                ),
                (
                    "entregue",
                    models.BooleanField(
                        blank=True,
                        default=True,
                        null=True,
                        verbose_name="Orçamento entregue",
                    ),
                ),
                ("dt_entregue", models.DateField(verbose_name="Data entregue")),
                (
                    "ordem_gerada",
                    models.BooleanField(
                        blank=True, default=True, null=True, verbose_name="Ordem gerada"
                    ),
                ),
                ("dt_nota", models.DateField(verbose_name="Data nota gerada")),
                (
                    "pago",
                    models.BooleanField(
                        blank=True,
                        default=True,
                        null=True,
                        verbose_name="Pagamento feito",
                    ),
                ),
                (
                    "tipo",
                    models.CharField(
                        choices=[("S", "Serviço"), ("P", "Peça")],
                        max_length=1,
                        verbose_name="Tipo do orçamento",
                    ),
                ),
            ],
            options={
                "verbose_name": "Orçamento",
                "verbose_name_plural": "Orçamentos",
            },
        ),
    ]
