# 🗃️ Organizador de Arquivos por Extensão

Script que categoriza e copia arquivos em pastas separadas com base em suas extensões (.pdf, .jpg, .mp3, etc).

## 🔧 Funcionalidades
- Criação automática de pastas por tipo de arquivo
- Organização por extensão
- Cópia dos arquivos para as pastas corretas

## 🛠️ Tecnologias
- Python
- Bibliotecas: `os`, `shutil`

## 📝 Observações
- Editar a variável `origem` com o caminho desejado
- Pode trocar `shutil.copy` por `shutil.move` se quiser mover os arquivos

## ▶️ Como executar

```bash
python organizador.py
