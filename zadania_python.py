# Zadanie 1
def czy_podzielna(a, b):
    if b == 0:
        return "Nie można dzielić przez zero!"
    if a % b == 0:
        return True
    else:
        return False


# Zadanie 2
def liczby_pierwsze(n):
    l_pierwsze = []
    for num in range(2, n):
        jest_pierwsza = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                jest_pierwsza = False
                break
        if jest_pierwsza:
            l_pierwsze.append(num)
    return l_pierwsze

# Zadanie 3
def posortuj_liste(lista):
    lista.sort()
    return lista

# Zadanie 4
def czesc_wspolna(lista1, lista2):
    return list(set(lista1) & set(lista2))

# Zadanie 5
from datetime import datetime

def ktore_urodziny(lata_urodzenia):
    aktualny_rok = datetime.now().year
    urodziny = []
    for rok in lata_urodzenia:
        wiek = aktualny_rok - rok
        urodziny.append(wiek)
    return urodziny
