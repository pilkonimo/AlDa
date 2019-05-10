'''
Aufgabe 1 - Einführung in Python

c)
1) Die Funktion sqrt() befindet sich im Modul math, wird wie folgt
importiert und genutzt:
'''
from math import sqrt
print(sqrt(64))
'''
2) Ruft man diese Funktion mit einer negativen Zahl wird ein ValueError mit
der Nachricht 'math domain error'geworfen. (Nutzt man jedoch das Modul cmath
wird die zugehörige komplexe Lösung berechnet.)

3) Benutzerdefinierte Varianten:
'''

def mysqrt(x):
    if x<0:
        print('mysqrt() funktioniert nicht für negative Zahlen, du Dussel!')
    else:
        return sqrt(x)

def mysqrt(x):
    try:
        return sqrt(x)
    except ValueError:
        print('mysqrt() funktioniert nicht für negative Zahlen, du Dussel!')

'''
(in beiden Fällen bei Misserfolg Rückgabewert None)

4) Erklärung des Modulo-Operators
'''

for i in range(-10,11):
    print("i="+str(i) + "\n" + "i%5="+str(i % 5))

'''
Der Modulo-Operator führt eine Division mit Rest durch und gibt diesen zurück. 
Bsp. m%n führt die Division m/n ganzzahlig durch und gibt deren Rest zurück.

5) Ein String sollte in dreifachen Anführungszeichen eingeschloßen sein, 
wenn er sich über mehr als eine Zeile erstreckt.

6) Die Klassen list und dict unterscheiden sich vorallem in der Art des 
Zugriffes. Bei einem list-Objekt handelt es sich um einen sequencer, auf den
man mittels durchnummerierter Indizierung zugreifen kann, wohingegen bei ein 
dict-Objekt eine Indizierung mittels selbstdefinierter Keys eines beliebigen
unveränderlichen Datentyps stattfindet.

7) Die __init__()-Funktion einer Klasse dient zur benutzerdefinierten 
Initialisierung eines Objektes der zugehörigen Klasse und wird bei jener 
automatisch instantan aufgerufen.
'''
