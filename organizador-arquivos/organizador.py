import os
import shutil

# !!! Inserir caminho onde estão os arquivos a serem organizados !!!
origem = r'seu_diretorio' # Exemplo: 'C:/Users/towers/OneDrive/Área de Trabalho'

categorias = {
    'imagens': ('.jpg', '.png', '.jpeg'),
    'documentos': ('.pdf', '.docx', '.txt'),
    'audios': ('.mp3', '.mp4', '.wav')
}

arquivos = os.listdir(origem)
print("\nArquivos encontrados:", arquivos)

for pasta in ['imagens', 'documentos', 'audios']:
    os.makedirs(pasta, exist_ok=True)
    print(f'\nPasta {pasta} criada com sucesso!')

for arquivo in arquivos:
    caminho_origem = os.path.join(origem, arquivo) 

    for pasta, extensoes in categorias.items():
        if arquivo.lower().endswith(extensoes): 
            shutil.copy(caminho_origem, os.path.join(pasta, arquivo))
            print(f'\n✅ Arquivo "{arquivo}" copiado para {pasta}/')

print('\nTodos os arquivos foram copiados com sucesso!')
print('\nFim do programa!\n')
