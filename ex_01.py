import re

def importar_texto_do_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        texto = arquivo.read()
    return texto

def dividir_texto_por_marcadores(caminho_arquivo):
    texto = importar_texto_do_arquivo(caminho_arquivo)
    marcadores = re.findall(r'NUM_ENTRE_\d+', texto)
    textos = re.split(r'NUM_ENTRE_\d+', texto)

    if textos[0] == '':
        textos.pop(0)

    if textos[-1] == '':
        textos.pop()

    contagem = []
    for i in range(len(marcadores)):
        contagem.append((marcadores[i], textos[i]))

    contador_tuplas_por_comprimento = {}
    for tupla in contagem:
        palavras = tupla[1].split()
        comprimento = len(palavras)
        if comprimento not in contador_tuplas_por_comprimento:
            contador_tuplas_por_comprimento[comprimento] = 1
        else:
            contador_tuplas_por_comprimento[comprimento] += 1

    contagem_formatado = ""
    for comprimento, quantidade in contador_tuplas_por_comprimento.items():
        contagem_formatado += f"\nExistem {quantidade} elementos com {comprimento} palavras."

    return textos, contagem_formatado

caminho_arquivo = 'corpus_test_1.txt'
lista_textos, contagem = dividir_texto_por_marcadores(caminho_arquivo)
print(lista_textos)
print(contagem)