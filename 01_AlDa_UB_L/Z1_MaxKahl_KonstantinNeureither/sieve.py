#!/usr/local/bin/python
#!/usr/bin/env python

"""ALDA Zettel 1, Aufgabe 1b
Max Kahl und Konstantin Neureither"""

def sieve(search_max):
    """Sucht Primzahlen bis zum übergebenen Maximum"""
    prime_list = list(range(2, search_max+1))

    prime_pos = 0
    check_pos = 1

    while prime_pos <= len(prime_list):

        while check_pos < len(prime_list):
            if prime_list[check_pos] % prime_list[prime_pos] == 0:
                del prime_list[check_pos]
                continue #ohne Inkrementierung, da Array eins Kürzer

            elif prime_list[check_pos] % prime_list[prime_pos] != 0:
                check_pos += 1

        prime_pos += 1
        check_pos = prime_pos + 1

    print(prime_list)
    return prime_list
