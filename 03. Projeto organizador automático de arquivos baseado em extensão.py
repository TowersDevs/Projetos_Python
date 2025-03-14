import os
import shutil

# Diretório de origem
origem = r'C:/Users/felip/OneDrive/Área de Trabalho/MIX'

# Categorias de arquivos
categorias = {
    'imagens': ('.jpg', '.png', '.jpeg'),
    'documentos': ('.pdf', '.docx', '.txt'),
    'audios': ('.mp3', '.mp4', '.wav')
}

# Listar arquivos do diretório especificado
arquivos = os.listdir(origem)
print("\nArquivos encontrados:", arquivos)

# Criar pastas se não existirem
for pasta in ['imagens', 'documentos', 'audios']:
    os.makedirs(pasta, exist_ok=True)
    print(f'\nPasta {pasta} criada com sucesso!')

# Copiar arquivos para a nova pasta
for arquivo in arquivos:
    caminho_origem = os.path.join(origem, arquivo)  # Caminho completo do arquivo original

    for pasta, extensoes in categorias.items():
        if arquivo.lower().endswith(extensoes):  # `.lower()` evita problemas com maiúsculas
            shutil.copy(caminho_origem, os.path.join(pasta, arquivo))
            print(f'\n✅ Arquivo "{arquivo}" copiado para {pasta}/')

print('\nTodos os arquivos foram copiados com sucesso!')
print('\nFim do programa!\n')