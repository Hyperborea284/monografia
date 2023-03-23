from collections import Counter
import matplotlib.pyplot as plt

def calcula_OME(texto):
    palavras = texto.split()
    frequencias = Counter(palavras)
    ordens = {}
    for i, palavra in enumerate(palavras):
        if palavra not in ordens:
            ordens[palavra] = []
        ordens[palavra].append(i+1) 

    OMEs = {}
    for palavra in frequencias:
        soma = sum([ordem for ordem in ordens[palavra]])
        OME = soma / frequencias[palavra]
        OMEs[palavra] = OME
    
    palavras_ordenadas = sorted(OMEs, key=OMEs.get, reverse=True)
    
    return palavras_ordenadas, OMEs

palavras_ordenadas, OMEs = calcula_OME(' '.join(palavras_filtradas))

def visualiza_OMEs(palavras_ordenadas, OMEs, fatia):
    palavras_fatia = palavras_ordenadas[fatia]
    OMEs_fatia = {palavra: OMEs[palavra] for palavra in palavras_fatia}
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.barh(range(len(OMEs_fatia)), list(OMEs_fatia.values()), align='center')
    ax.set_yticks(range(len(OMEs_fatia)))
    ax.set_yticklabels(palavras_fatia)
    ax.invert_yaxis()
    ax.set_xlabel('OME')
    ax.set_title('OMEs das palavras ({}:{})'.format(fatia.start, fatia.stop))

    for i, palavra in enumerate(palavras_fatia):
        ax.text(OMEs_fatia[palavra] + 0.05, i, round(OMEs_fatia[palavra], 2), ha='left', va='center')
    
    plt.show()

visualiza_OMEs(palavras_ordenadas, OMEs, slice(0, 20))