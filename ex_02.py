import re
from ftlangdetect import detect
import spacy

def extrair_entidades(texto_entrev):
    texto_entrev = re.sub(r'\n', '', texto_entrev)
    texto_entrev = texto_entrev.replace('\n', ' ')
    codigo_idioma = detect(text=texto_entrev, low_memory=False)

    if codigo_idioma['lang'] == 'en':
        codigo_idioma_curto = 'english'
        codigo_idioma_completo = 'en_core_web_sm'
    elif codigo_idioma['lang'] == 'pt':
        codigo_idioma_curto = 'portuguese'
        codigo_idioma_completo = 'pt_core_news_sm'
    else:
        codigo_idioma_curto = codigo_idioma['lang']
        codigo_idioma_completo = ''

    lista_entidades = []
    modelo_pln = spacy.load(codigo_idioma_completo)
    documento = modelo_pln(texto_entrev)
    for entidade in documento.ents:
        if [entidade.text, entidade.label_] not in lista_entidades:
            lista_entidades.append([entidade.text, entidade.label_])

    codigo_idioma = codigo_idioma['lang']

    return lista_entidades, codigo_idioma, codigo_idioma_curto, codigo_idioma_completo

def contagem_entidades(lista_entidades):
    contagem_ent = {}
    for entidade in lista_entidades:
        if entidade[1] not in contagem_ent:
            contagem_ent[entidade[1]] = [entidade[0]]
        else:
            contagem_ent[entidade[1]].append(entidade[0])

    fstring_decorada = f"Quantidade de entidades por tipo: \n"
    for tipo, elementos in contagem_ent.items():
        fstring_decorada += f"{tipo}: {len(elementos)}\n"
        fstring_decorada += f"{', '.join(elementos)}\n\n"

    return fstring_decorada, contagem_ent

def imprimir_contagem_entidades(lista_textos):
    for i, texto_entrev in enumerate(lista_textos):
        lista_entidades, codigo_idioma, codigo_idioma_curto, codigo_idioma_completo = extrair_entidades(texto_entrev)
        fstring_decorada, contagem = contagem_entidades(lista_entidades)
        print(f"Texto {i+1} ({codigo_idioma_curto}):")
        print(fstring_decorada)

imprimir_contagem_entidades(lista_textos)