
import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def gerar_excel(dados):
    df = pd.DataFrame([dados])
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Ficha de Admissão')
    return output.getvalue()

def gerar_pdf(dados):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    largura, altura = A4
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(largura / 2, altura - 50, "FICHA DE ADMISSÃO - 2024")
    c.setFont("Helvetica", 11)
    y = altura - 100
    for chave, valor in dados.items():
        c.drawString(60, y, f"{chave}: {valor}")
        y -= 20
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf

st.title("🧾 Ficha de Admissão - Lara Associados")
st.caption("Preencha os dados abaixo e gere os arquivos PDF e Excel")

dados = {
    "Razão Social": st.text_input("Razão Social"),
    "Empregador": st.text_input("Empregador"),
    "Empregado": st.text_input("Empregado"),
    "CPF": st.text_input("CPF"),
    "Nascimento": st.text_input("Data de Nascimento"),
    "Estado Civil": st.text_input("Estado Civil"),
    "Sexo": st.text_input("Sexo"),
    "Raça": st.text_input("Raça"),
    "Grau de Instrução": st.text_input("Grau de Instrução"),
    "Nome da mãe": st.text_input("Nome da mãe"),
    "Nome do pai": st.text_input("Nome do pai"),
    "Endereço": st.text_input("Endereço"),
    "Contato": st.text_input("Contato"),
    "Dependente": st.text_input("Dependente"),
    "CPF Dependente": st.text_input("CPF Dependente"),
    "Nascimento Dependente": st.text_input("Nascimento Dependente"),
    "Dependente2": st.text_input("Dependente2"),
    "CPF Dependente2": st.text_input("CPF Dependente2"),
    "Nascimento Dependente2": st.text_input("Nascimento Dependente2"),
    "Admissão": st.date_input("Data de Admissão", value=date.today()),
    "Função": st.text_input("Função"),
    "Salário": st.number_input("Salário (R$)", min_value=0.0, step=0.01),
    "Horário": st.text_input("Horário de Trabalho"),
    "Intervalo": st.text_input("Intervalo"),
    "Naturalidade": st.text_input("Naturalidade"),
}

if st.button("📄 Gerar Ficha de Admissão"):
    st.success("Ficha gerada com sucesso!")
    excel_bytes = gerar_excel(dados)
    pdf_bytes = gerar_pdf(dados)

    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            label="⬇️ Baixar Excel",
            data=excel_bytes,
            file_name="Ficha_de_Admissao.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
    with col2:
        st.download_button(
            label="📄 Baixar PDF",
            data=pdf_bytes,
            file_name="Ficha_de_Admissao.pdf",
            mime="application/pdf",
        )
