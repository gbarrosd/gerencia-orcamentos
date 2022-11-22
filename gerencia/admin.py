from django.contrib import admin
from .models import Orcamento, Secretaria
from gerencia.gerar_pdf_ordens_atr import gerar_pdf, gerar_pdf_pagamento

# Register your models here.


@admin.action(description="Gerar PDF de ordens atrasadas")
def gerar_pdf_ordens_atrasadas(modeladmin, request, queryset):
    orcamentos = queryset
    orcamentos_atrasados = []
    for orcamento in orcamentos:
        if orcamento.ordem_gerada == False and orcamento.entregue == True:
            orcamentos_atrasados.append(orcamento)
    gerar_pdf(orcamentos_atrasados)


@admin.action(description="Gerar PDF de pagamentos atrasados")
def gerar_pdf_pagamentos_atrasados(modeladmin, request, queryset):
    orcamentos = queryset
    orcamentos_atrasados = []
    for orcamento in orcamentos:
        if (
            orcamento.ordem_gerada == True
            and orcamento.entregue == True
            and orcamento.dt_nota != None
            and orcamento.pago == False
        ):
            orcamentos_atrasados.append(orcamento)
    gerar_pdf_pagamento(orcamentos_atrasados)


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
        "numero",
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
    actions = [gerar_pdf_ordens_atrasadas, gerar_pdf_pagamentos_atrasados]
