import re


def count_words(texto):
    texto=texto.lower()
    regex = r'[\w|\']+'
    palabras = re.findall(regex, texto)
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] = conteo[palabra] + 1
        else:
            conteo[palabra] = 1
    return conteo
    print(palabras)
    print(conteo)

