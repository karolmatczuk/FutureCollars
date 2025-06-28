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
