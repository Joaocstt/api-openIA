from fpdf import FPDF

def gerar_pdf(dados: dict, filename="pedido_extraido.pdf") -> str:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(0, 10, "Informações do Pedido", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(0, 10, f"Cliente: {dados.get('cliente', '')}", ln=True)
    pdf.cell(0, 10, f"Endereço: {dados.get('endereco', '')}", ln=True)
    pdf.cell(0, 10, f"Data e Hora da Entrega: {dados.get('data_hora_entrega', '')}", ln=True)
    pdf.cell(0, 10, f"Telefone do Comprador: {dados.get('telefone_comprador', '')}", ln=True)
    pdf.cell(0, 10, f"Telefone do Recebedor: {dados.get('telefone_recebedor', '')}", ln=True)
    pdf.cell(0, 10, f"Produto: {dados.get('produto', '')}", ln=True)

    pdf.output(filename)
    return filename
