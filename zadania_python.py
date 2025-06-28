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
