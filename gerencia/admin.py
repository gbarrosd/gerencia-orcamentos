from django.contrib import admin
from .models import Orcamento, Secretaria

# Register your models here.


@admin.register(Secretaria)
class SecretariaAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "cnpj",
    )
    search_fields = ("nome", "cnpj")
    list_filter = ("cnpj",)
    ordering = ("nome",)


@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = (
        "criado_em",
        "secretaria",
        "entregue",
        "ordem_gerada",
        "pago",
        "tipo",
    )
    search_fields = ("numero",)
    list_filter = ("secretaria",)
    ordering = ("criado_em",)
