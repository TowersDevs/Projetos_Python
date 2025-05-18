# 📥 Bot de Leitura de E-mails com Salvamento Inteligente de Anexos

Este bot automatiza o acesso à caixa de entrada do Gmail, identifica e-mails com anexos e salva os arquivos localmente organizados por data de recebimento.  
Ideal para automatizar rotinas de recebimento de notas fiscais, boletos, documentos ou relatórios enviados por e-mail.

## 💡 Problema que resolve
Profissionais perdem tempo acessando e-mails manualmente para baixar e organizar anexos — especialmente quando o volume é alto ou recorrente.  
Este bot elimina completamente essa tarefa, executando tudo de forma automatizada e organizada.

## 🚀 Solução implementada
- Conexão segura via protocolo IMAP ao Gmail
- Leitura e varredura de e-mails da caixa de entrada
- Download automático de anexos
- Organização em pastas nomeadas por data (ex: `2025-05-18/`)

## 🛠️ Tecnologias
- Python
- Bibliotecas: `imaplib`, `email`, `os`, `datetime`

## 📈 Resultados
- Processamento de dezenas de e-mails e anexos em segundos
- Organização padronizada, pronta para backup ou integração com outros sistemas

## ▶️ Como executar
1. Configure seu Gmail para permitir acesso IMAP
2. Edite o script com suas credenciais e parâmetros desejados
3. Execute:
```bash
python email_anexos.py
