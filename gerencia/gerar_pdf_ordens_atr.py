from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from reportlab.platypus import TableStyle


def gerar_pdf(orcamentos):
    fileName = "ordens-atrasadas.pdf"
    documentTitle = "Ordens atrasadas"
    title = "Orçamentos"
    subTitle = "Com ordem de serviço não enviada"

    dados = []
    for orcamento in orcamentos:
        dados.append(
            [
                f"N° {orcamento.numero} - Data entrega: {orcamento.dt_entregue} - Tipo: {orcamento.tipo} - Secretaria: {orcamento.secretaria.nome} - Valor: R${orcamento.valor}"
            ],
        )
    pdf = SimpleDocTemplate(fileName, pagesize=A4)

    tabela = Table(dados)
    elems = []
    elems.append(tabela)

    pdf.build(elems)
