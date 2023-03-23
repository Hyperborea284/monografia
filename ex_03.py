import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

def limpador_texto(texto, codigo_idioma_curto):
    tokens_texto = nltk.tokenize.word_tokenize(texto, language=codigo_idioma_curto)
    palavras_paradas = set(nltk.corpus.stopwords.words(codigo_idioma_curto))
    palavras_filtradas_0 = [palavra.lower() for palavra in tokens_texto if palavra.lower() not in palavras_paradas and palavra.lower()]
    palavras_filtradas_1 = [re.sub('[0-9]', '', palavra) for palavra in palavras_filtradas_0]
    palavras_filtradas = [palavra for palavra in palavras_filtradas_1 if len(palavra) >= 2]
    triplas_saida = list(nltk.trigrams(palavras_filtradas))
    bigramas_saida = list(nltk.bigrams(palavras_filtradas))
    contagem_palavras = Counter(palavras_filtradas)
    hapaxes = [palavra for palavra in contagem_palavras if contagem_palavras[palavra] == 1]
    palavras_filtradas_sem_hap = [palavra for palavra in palavras_filtradas if palavra not in hapaxes]

    return triplas_saida, bigramas_saida, palavras_filtradas, hapaxes, palavras_filtradas_sem_hap

lista_entidades, codigo_idioma, codigo_idioma_curto, codigo_idioma_completo = extrair_entidades(lista_textos[2])
triplas_saida, bigramas_saida, palavras_filtradas, hapaxes, palavras_filtradas_sem_hap = limpador_texto(lista_textos[2], codigo_idioma_curto)

def visualizar_listas(triplas, bigramas, palavras_filtradas, hapaxes, palavras_filtradas_sem_hap):
    tamanho = min(len(triplas), len(bigramas), len(palavras_filtradas), len(hapaxes), len(palavras_filtradas_sem_hap))

    for i in range(tamanho):
        print(f"\nTexto {i+1}")
        print("Triplas:")
        print(triplas[i][:5])
        print("Bigramas:")
        print(bigramas[i][:5])
        print("Palavras filtradas:")
        print(palavras_filtradas[i][:5])
        print("Hapaxes:")
        print(hapaxes[i][:5])
        print("Palavras filtradas sem hapaxes:")
        print(palavras_filtradas_sem_hap[i][:5])

visualizar_listas(triplas_saida, bigramas_saida, palavras_filtradas, hapaxes, palavras_filtradas_sem_hap)