from fpdf import FPDF

def gerar_pdf_os(cliente, tecnico, tipo_servico, descricao_servico, valor_servico, status, data_criacao):
    pdf = FPDF()
    pdf.add_page()
    
    # Cabeçalho
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(0, 10, txt="Ordem de Serviço", ln=True, align="C")
    pdf.ln(10)
    
    # Detalhes da OS
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, txt=f"Cliente: {cliente}", ln=True)
    pdf.cell(0, 10, txt=f"Técnico: {tecnico}", ln=True)
    pdf.cell(0, 10, txt=f"Tipo de Serviço: {tipo_servico}", ln=True)
    pdf.cell(0, 10, txt=f"Descrição: {descricao_servico}", ln=True)
    pdf.cell(0, 10, txt=f"Valor do Serviço: R$ {valor_servico:.2f}", ln=True)
    pdf.cell(0, 10, txt=f"Status: {status}", ln=True)
    pdf.cell(0, 10, txt=f"Data de Criação: {data_criacao}", ln=True)
    
    # Salvar PDF
    pdf.output("ordem_servico.pdf")
