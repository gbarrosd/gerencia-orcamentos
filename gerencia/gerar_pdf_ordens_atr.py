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
    if len(dados) == 0:
        dados.append(["SEM ORÇAMENTOS COM ORDEM DE SERVIÇO ATRASADA"])
    dados.insert(0, ["ORÇAMENTOS SEM ORDEM DE SERVIÇO"])
    pdf = SimpleDocTemplate(fileName, pagesize=A4)

    tabela = Table(dados)

    style = TableStyle(
        [
            ("BACKGROUND", (0, 0), (3, 0), colors.green),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Courier-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 14),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ]
    )
    tabela.setStyle(style)

    rowNumb = len(dados)
    for i in range(1, rowNumb):
        if i % 2 == 0:
            bc = colors.burlywood
        else:
            bc = colors.beige

        ts = TableStyle([("BACKGROUND", (0, i), (-1, i), bc)])
        tabela.setStyle(ts)

    ts = TableStyle(
        [
            ("BOX", (0, 0), (-1, -1), 2, colors.black),
            ("LINEBEFORE", (2, 1), (2, -1), 2, colors.red),
            ("LINEABOVE", (0, 2), (-1, 2), 2, colors.green),
            ("GRID", (0, 1), (-1, -1), 2, colors.black),
        ]
    )
    tabela.setStyle(ts)
    elems = []
    elems.append(tabela)
    pdf.title = "orçamentos ordem faltando"
    pdf.build(elems)
