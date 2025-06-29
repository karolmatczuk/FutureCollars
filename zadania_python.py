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

# Zadanie 6
panstwo1 = {
    "nazwa": "Polska",
    "powierzchnia": 312696,
    "ludnosc": 37950000,
    "pkb_per_capita": 42000
}

panstwo2 = {
    "nazwa": "Niemcy",
    "powierzchnia": 357022,
    "ludnosc": 83020000,
    "pkb_per_capita": 58000
}

panstwo3 = {
    "nazwa": "Czechy",
    "powierzchnia": 78866,
    "ludnosc": 10700000,
    "pkb_per_capita": 46000
}

panstwo4 = {
    "nazwa": "Norwegia",
    "powierzchnia": 385207,
    "ludnosc": 5470000,
    "pkb_per_capita": 83000
}

def wypisz_ranking(panstwa):
    print("\n--- Państwa według powierzchni ---")
    for p in sorted(panstwa, key=lambda x: x["powierzchnia"], reverse=True):
        print(f"{p['nazwa']}: {p['powierzchnia']} km2")

    print("\n--- Państwa według liczby ludności ---")
    for p in sorted(panstwa, key=lambda x: x["ludnosc"], reverse=True):
        print(f"{p['nazwa']}: {p['ludnosc']} osób")

    print("\n--- Państwa według gęstości zaludnienia ---")
    for p in sorted(panstwa, key=lambda x: x["ludnosc"]/x["powierzchnia"], reverse=True):
        gestosc = p["ludnosc"]/p["powierzchnia"]
        print(f"{p['nazwa']}: {gestosc:.2f} osób/km2")

    print("\n--- Państwa według PKB per capita (PPP) ---")
    for p in sorted(panstwa, key=lambda x: x["pkb_per_capita"], reverse=True):
        print(f"{p['nazwa']}: {p['pkb_per_capita']} USD")

# Zadanie 7
def policz_litery_cyfry(napis):
    liczba_liter = 0
    liczba_cyfr = 0
    for znak in napis:
        if znak.isalpha():
            liczba_liter += 1
        elif znak.isdigit():
            liczba_cyfr += 1
    return liczba_liter, liczba_cyfr

# Zadanie 8
def czy_palindromy(napis1, napis2):
    def jest_palindromem(s):
        return s == s[::-1]
    
    return jest_palindromem(napis1), jest_palindromem(napis2)

# Zadanie 9
def wzor():
    total_lines = 9
    for i in range(1, total_lines + 1):
        if i <= 5:
            num_elements = i
        else:
            num_elements = total_lines - i + 1
        for j in range(num_elements):
            if j % 2 == 0:
                print('*', end=' ')
            else:
                print('$', end=' ')
        print()

# Zadanie 10
import numpy as np

def posortowana_roznica_numpy(lista1, lista2):
    arr1 = np.array(lista1)
    arr2 = np.array(lista2)

    maska = ~np.isin(arr1, arr2)
    filtr = arr1[maska]

    unikalne, licznik = np.unique(filtr, return_counts=True)

    indeksy_sort = np.argsort(licznik)

    wynik = unikalne[indeksy_sort]

    return wynik.tolist()

# Zadanie 11
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Zadanie 12
osoby = {}

def dodaj_osobe(imie, wzrost):
    global osoby
    osoby[imie] = wzrost

# Dodaje 5 wpisów
dodaj_osobe(imie="Ala", wzrost=165)
dodaj_osobe(imie="Bartek", wzrost=180)
dodaj_osobe(imie="Celina", wzrost=172)
dodaj_osobe(imie="Darek", wzrost=177)
dodaj_osobe(imie="Ela", wzrost=160)

# Zadanie 13
def sortuj_wg_wzrostu(slownik):
    posortowane = sorted(slownik.items(), key=lambda x: x[1], reverse=True)
    imiona = [k for k, v in posortowane]
    return imiona

# Zadanie 14
def potegowanie(a, b):
    # Przypadek zerowego wykładnika
    if b == 0:
        return 1
    # Przypadek dodatni
    elif b > 0:
        return a * potegowanie(a, b - 1)
    # Przypadek ujemny
    else:
        return 1 / potegowanie(a, -b)

# Zadanie 15
def najczesciej_wystepujacy(lista):
    licznik = {}
    for x in lista:
        if x in licznik:
            licznik[x] += 1
        else:
            licznik[x] = 1
    najczestszy = max(licznik, key=licznik.get)
    return najczestszy
