# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#libraries
import random

print("Wybierz drzwi A, B lub C.")
drzwi = input('')
if drzwi not in ['A','B','C']:
    print("Błąd, wybrano drzwi z poza listy.")
    exit()
else:
    wygrana = random.choice(['A', 'B', 'C'])
    print("Nagroda jest za drzwiami", wygrana)
    bez_wygranej = list(['A', 'B', 'C'])
    bez_wygranej.remove(wygrana)

    otwarte = random.choice([i for i in bez_wygranej if i not in drzwi])
    pozostałe = list(['A', 'B', 'C'])
    pozostałe.remove(otwarte)
    pozostałe.remove(drzwi)
    pozostałe = pozostałe[0]
    print("Zostały otworzone drzwi ",otwarte, ". Czy chcesz zmienić drzwi na", pozostałe, "? tak/nie")
    zmiana = input('')
    c = 0
    if zmiana == 'tak':
        c = drzwi
        drzwi = pozostałe
        pozostałe = c
    if drzwi == wygrana:
        print("Gratulacje, wygrałeś")
    else:
        print("Niestety przegrałeś")





