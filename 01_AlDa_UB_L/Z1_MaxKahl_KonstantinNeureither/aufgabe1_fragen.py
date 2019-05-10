#!/usr/local/bin/python
#!/usr/bin/env python

"""ALDA Zettel 1, Aufgabe 1c
Max Kahl und Konstantin Neureither

c)
1) Die Funktion sqrt() befindet sich im Modul math, wird wie folgt
importiert und genutzt:
"""
import math as m
m.sqrt(64)

'''
2) Ruft man diese Funktion mit einer negativen Zahl wird ein ValueError mit
der Nachricht 'math domain error' geworfen. (Nutzt man jedoch das Modul cmath
wird die zugehörige komplexe Lösung berechnet.)

3) Benutzerdefinierte Varianten:
'''

def mysqrt(x):
    """Wurzelfunktion mit negativ Prüfung mit if..."""
    if x < 0:
        print("mysqrt() funktioniert nicht für negative Zahlen, du Dussel!")
        return 0
    else:
        return m.sqrt(x)


def mysqrt_try(x):
    """Wurzelfunktion mit negativ Prüfung mit try...catch"""
    try:
        return m.sqrt(x)
    except ValueError:
        print("mysqrt() funktioniert nicht für negative Zahlen, du Dussel!")

        #nicht unbedigt nötig, liefert zusätzlich die Compiler Fehlermeldng
        print('\n \n ERROR MSG:')
        raise

'''

4) Erklärung des Modulo-Operators
'''

def task1_4():
    for i in range(-10,11):
        print(i, i%5)

'''
Der Modulo-Operator führt eine Division mit Rest durch und gibt diesen zurück. 
Bsp. m%n führt die Division m/n ganzzahlig durch und gibt deren Rest zurück.

5) Ein String sollte in dreifachen Anführungszeichen eingeschloßen sein, 
wenn er sich über mehr als eine Zeile erstreckt.

6) Die Klassen list und dict unterscheiden sich vorallem in der Art des 
Zugriffes und der Indizierung. Bei einem list-Objekt handelt es sich um einen sequencer, auf den
man mittels durchnummerierter Indizierung zugreifen kann, wohingegen bei ein 
dict-Objekt eine Indizierung mittels selbstdefinierter Keys eines beliebigen
unveränderlichen Datentyps stattfindet.

7) Die __init__()-Funktion einer Klasse dient zur benutzerdefinierten 
Initialisierung eines Objektes der zugehörigen Klasse und wird bei jener 
automatisch instantan aufgerufen.
'''
