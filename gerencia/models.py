from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Secretaria(models.Model):
    nome = models.CharField(max_length=255, verbose_name=_("Nome"))
    cnpj = models.CharField(max_length=50, verbose_name=_("CNPJ"), null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = _("Secretaria")
        verbose_name_plural = _("Secretarias")


class Orcamento(models.Model):
    class TipoChoice(models.TextChoices):
        ATIVO = "S", _("Serviço")
        INATIVO = "P", _("Peça")

    numero = models.CharField(
        max_length=100, verbose_name=_("número do orçamento"), null=True, blank=True
    )
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name=_("criado em"))
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name=_("atualizado em"))
    entregue = models.BooleanField(
        default=True, null=True, blank=True, verbose_name=_("Orçamento entregue")
    )
    dt_entregue = models.DateField(
        null=True, blank=True, verbose_name=_("Data entregue")
    )
    ordem_gerada = models.BooleanField(
        default=True, null=True, blank=True, verbose_name=_("Ordem gerada")
    )
    dt_nota = models.DateField(
        null=True, blank=True, verbose_name=_("Data nota gerada")
    )
    pago = models.BooleanField(
        default=True, null=True, blank=True, verbose_name=_("Pagamento feito")
    )
    tipo = models.CharField(
        max_length=1,
        choices=TipoChoice.choices,
        verbose_name=_("Tipo do orçamento"),
    )
    valor = models.FloatField(verbose_name=_("Valor"), null=True, blank=True)
    secretaria = models.ForeignKey(
        "Secretaria",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_("Secretaria"),
        related_name="orcamentos",
    )

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name = _("Orçamento")
        verbose_name_plural = _("Orçamentos")
