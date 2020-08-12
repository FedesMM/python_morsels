from unicodedata import normalize
import re


def is_anagram (palabra_1, palabra_2):
    p_1 = re.sub(r"[^A-Za-z]+", '', normalize('NFD', palabra_1).upper())
    p_2 = re.sub(r"[^A-Za-z]+", '', normalize('NFD', palabra_2).upper())
    print(f"\npalabra_1 ({p_1})\tpalabra_2 ({p_2})")
    for letra in p_1:
        print(f"\tChequeando: {letra}\tpalabra_1 ({p_1}) {p_1.count(letra)}\tpalabra_2 ({p_2}) {p_2.count(letra)}")
        if p_1.upper().count(letra) != p_2.upper().count(letra):
            return False
    return True
