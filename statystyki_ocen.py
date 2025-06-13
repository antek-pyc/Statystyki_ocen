# Import bibliotek
from collections import Counter
from math import sqrt

# Przygotowanie danych do obliczeń 
oceny_1 = [4, 3, 5, 2, 1, 6, 3, 4,]
oceny_1.sort()
tabela = dict(Counter(oceny_1))

# Funcje do liczenia statystyk
def srednia_arytmetyczna(oceny):
    suma = 0
    for ocena in oceny:
        suma += ocena
    srednia_arytmetyczna = suma/len(oceny)
    return srednia_arytmetyczna

def dominanta(oceny):
    return [k for k, v in tabela.items() if v == max(tabela.values())]

def mediana(oceny):
    if len(oceny) == 0:
        return None
    elif len(oceny)%2 == 0:
        return (oceny[len(oceny) // 2 - 1] + oceny[len(oceny) // 2]) / 2
    else:
        return oceny[(len(oceny)) // 2]
    
def wariancja(oceny):
    sa = srednia_arytmetyczna(oceny)
    suma_wariancji = 0
    for ocena in oceny:
        suma_wariancji += (ocena - sa) ** 2
    wariancja = suma_wariancji/len(oceny)
    return wariancja

def odchylenie_standardowe(oceny):
    return sqrt(wariancja(oceny))

# Wiadomość w terminalu
print(f"Oceny: {oceny_1}")
print(f"Ilość ocen: {len(oceny_1)}")
print(f"Średnia ocen to: {srednia_arytmetyczna(oceny_1)}")
print(f"Wariancja to: {wariancja(oceny_1)}")
print(f"Odchylenie standardowe: {odchylenie_standardowe(oceny_1)}")
print(f"Mediana to: {mediana(oceny_1)}")
print(f"Dominanta to: {dominanta(oceny_1)}")
