# Esse código comunica com o site Ipeadata (Dados econômicos e financeiros do Brasil) via API, gera um gráfico dos dados
# conforme o "codigo_serie escolhido" e envia esse aquivo por e-mail.
# Basta alterar os dados no campo "# Alterar aqui" logo abaixo e rodar o script

import os
import smtplib
import matplotlib.pyplot as plt
from fpdf import FPDF
from ipeadatapy import timeseries
from email.message import EmailMessage
from datetime import datetime

# Alterar aqui
email = 'seu_email@gmail.com'
senha = 'sua_senha'
destinatario = 'email_de_destino@gmail.com'
codigo_serie = 'BM12_TJOVER12' # Código da série desejada (exemplo: Taxa SELIC)

diretorio = 'relatorios'
os.makedirs(diretorio, exist_ok=True)

data_atual = datetime.now().strftime('%Y-%m-%d')
nome_arquivo = f'relatorio_{codigo_serie}_{data_atual}'

# 1. Buscar dados da série
dados = timeseries(codigo_serie)

# 2. Gerar gráfico
plt.figure(figsize=(10, 6))
print(dados.columns)
plt.plot(dados.index, dados[dados.columns[-1]], label='Valor')
plt.title(f'Série: {codigo_serie}')
plt.xlabel('Data')
plt.ylabel('Valor')
plt.grid(True)
plt.legend()
grafico_path = os.path.join(diretorio, f'{nome_arquivo}.png')
plt.savefig(grafico_path)
plt.close()

# 3. Criar PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, f'Relatório: {codigo_serie}', ln=True, align='C')
pdf.image(grafico_path, x=10, y=30, w=190)
pdf_path = os.path.join(diretorio, f'{nome_arquivo}.pdf')
pdf.output(pdf_path)

# 4. Enviar e-mail
def enviar_email(destinatario, assunto, corpo, anexo_path):
    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = email
    msg['To'] = destinatario
    msg.set_content(corpo)

    with open(anexo_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(anexo_path)
        msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email, senha)
        smtp.send_message(msg)

assunto = f'Relatório: {codigo_serie}'
corpo = f'Olá,\n\nSegue em anexo o relatório da série {codigo_serie}.\n\nAtenciosamente.'
enviar_email(destinatario, assunto, corpo, pdf_path)

print ('E-mail enviado com sucesso!')