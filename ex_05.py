import numpy as np

def analise_prototipica_v1(palavras_ordenadas, OMEs):
    if not isinstance(palavras_ordenadas, list) or not isinstance(OMEs, dict):
        raise TypeError
    
    if len(palavras_ordenadas) != len(OMEs):
        raise ValueError
    
    palavras_OMEs = [(palavra, OMEs.get(palavra, 0)) for palavra in palavras_ordenadas]
    
    media_OME = np.mean(list(OMEs.values()))
    
    nucleo_central_o = [(palavra, ome/ media_OME) for palavra, ome in palavras_OMEs if ome > media_OME]
    zona_periferica_1 = [(palavra, ome/ media_OME) for palavra, ome in palavras_OMEs if ome <= media_OME and palavras_OMEs.index((palavra, ome)) <= len(palavras_OMEs) * 0.25]
    zona_periferica_2 = [(palavra, ome/ media_OME) for palavra, ome in palavras_OMEs if ome <= media_OME and palavras_OMEs.index((palavra, ome)) > len(palavras_OMEs) * 0.25 and palavras_OMEs.index((palavra, ome)) <= len(palavras_OMEs) * 0.75]
    zona_periferica_3 = [(palavra, ome/ media_OME) for palavra, ome in palavras_OMEs if ome <= media_OME and palavras_OMEs.index((palavra, ome)) > len(palavras_OMEs) * 0.75]
    
    return nucleo_central_o, zona_periferica_1, zona_periferica_2, zona_periferica_3
