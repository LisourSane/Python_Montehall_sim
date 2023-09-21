# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#libraries
import random
import numpy as np
import matplotlib.pyplot as plp

print("Jeśli chcesz zagrać samemu, wpisz 1. Jeśli chcesz przeprowadzić symulacje, wpisz 2.")
tryb = int(input())
if tryb == 1:
    print("Wybierz drzwi A, B lub C.")
    drzwi = input('')
    if drzwi not in ['A', 'B', 'C']:
        print("Błąd, wybrano drzwi z poza listy.")
        exit()
    else:
        wygrana = random.choice(['A', 'B', 'C'])
        #print("Nagroda jest za drzwiami", wygrana)
        bez_wygranej = list(['A', 'B', 'C'])
        bez_wygranej.remove(wygrana)
        otwarte = random.choice([i for i in bez_wygranej if i not in drzwi])
        pozostałe = list(['A', 'B', 'C'])
        pozostałe.remove(otwarte)
        pozostałe.remove(drzwi)
        pozostałe = pozostałe[0]
        print("Zostały otworzone drzwi ", otwarte, ". Czy chcesz zmienić drzwi na", pozostałe, "? tak/nie")
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
elif tryb == 2:
    print("Ile chcesz prób w symulacji?")
    n = int(input())
    print("Jeśli chcesz zawsze zmieniać, wpisz 1. Jeśli chcesz zawsze zostawiać, wpisz 2. Jeśli ma być losowo, wpisz 3.")
    mode = int(input())
    wyniki = np.zeros(n)
    if mode == 1:
        for i in range(0, n):
            win = random.choice(['A', 'B', 'C'])
            #print("win", win)
            pick = random.choice(['A', 'B', 'C'])
            #print("pick", pick)
            not_pick = ['A', 'B', 'C']
            not_pick.remove(pick)
            #print("not_pick", not_pick)
            op = [i for i in not_pick if i != win]
            op = random.choice(op)
            #print("op", op)
            left = ['A', 'B', 'C']
            left.remove(op)
            left.remove(pick)
            left = left[0]
            #print("left", left)
            c = pick
            pick = left
            left = c
            if win == pick:
                wyniki[i] = 1
                #print("Wygrana")
                #print(wyniki.cumsum())
            else:
                wyniki[i] = 0
                #print("Przegrana")
                #print(wyniki.cumsum())
        for_plot = wyniki.cumsum()/n
        plp.plot(for_plot)
        plp.xlabel("Próby")
        plp.ylabel("Prawdopodobieństwo")
        plp.title("Symulacja")
        plp.show()
    elif mode == 2:
        for i in range(0, n):
            win = random.choice(['A', 'B', 'C'])
            #print("win", win)
            pick = random.choice(['A', 'B', 'C'])
            if win == pick:
                wyniki[i] = 1
                # print("Wygrana")
                # print(wyniki.cumsum())
            else:
                wyniki[i] = 0
                # print("Przegrana")
                # print(wyniki.cumsum())
        for_plot = wyniki.cumsum() / n
        plp.plot(for_plot)
        plp.xlabel("Próby")
        plp.ylabel("Prawdopodobieństwo")
        plp.title("Symulacja")
        plp.show()
    else:
        for i in range(0, n):
            j = random.choice([1,2])
            win = random.choice(['A', 'B', 'C'])
            #print("win", win)
            pick = random.choice(['A', 'B', 'C'])
            if j%2 == 1:
                not_pick = ['A', 'B', 'C']
                not_pick.remove(pick)
                # print("not_pick", not_pick)
                op = [i for i in not_pick if i != win]
                op = random.choice(op)
                # print("op", op)
                left = ['A', 'B', 'C']
                left.remove(op)
                left.remove(pick)
                left = left[0]
                # print("left", left)
                c = pick
                pick = left
                left = c
            if win == pick:
                wyniki[i] = 1
                #print("Wygrana")
                #print(wyniki.cumsum())
            else:
                wyniki[i] = 0
                #print("Przegrana")
                #print(wyniki.cumsum())
        for_plot = wyniki.cumsum()/n
        plp.plot(for_plot)
        plp.xlabel("Próby")
        plp.ylabel("Prawdopodobieństwo")
        plp.title("Symulacja")
        plp.show()





else:
    print("Proszę wpisać 1 lub 2!")
    exit()





