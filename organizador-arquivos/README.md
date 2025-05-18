# 🗃️ Organizador Automático de Arquivos por Extensão

Este script automatiza a organização de arquivos em um diretório, categorizando-os automaticamente em pastas com base em suas extensões (.pdf, .jpg, .xlsx, .mp3, etc).  
É ideal para quem deseja manter seus arquivos organizados sem esforço manual, seja em ambientes pessoais ou profissionais.

## 💡 Problema que resolve
Arquivos acumulados em uma única pasta tornam difícil encontrar o que se precisa e causam perda de tempo com organização manual.  
Este script executa a tarefa de forma rápida, categorizando conforme o tipo de arquivo.

## 🚀 Solução implementada
- Leitura do diretório especificado e verificação de extensões
- Criação automática de pastas por categoria (documentos, imagens, áudios, etc)
- Cópia dos arquivos para as pastas corretas com base em suas extensões
- Flexível para adicionar novas categorias facilmente


## 🛠️ Tecnologias
- Python
- Bibliotecas: `os`, `shutil`

## 📈 Resultados
- Organização de dezenas de arquivos em segundos
- Redução de tarefas repetitivas e erros de arquivamento manual
- Adaptação simples para qualquer estrutura de pastas ou categorias

## ▶️ Como executar
1. Altere a variável `origem` com o caminho do diretório desejado
2. Execute:
```bash
python organizador.py
