# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 16:37:22 2023

@author: frapeloros
"""

#esempio di algoritmo LFSR 

class LFSR:
    def __init__(self, seed, taps,n):
        self.state = seed
        self.taps = taps
        self.n=n 

    def __next__(self):
        # Calcola il prossimo bit del keystream.
        feedback = 0
        for tap in self.taps:
            feedback ^= int(self.state[tap])
        output = int(self.state[-1])
        self.state = str(output) + self.state[:-1]
        # Restituisci il bit calcolato.
        return output

    def generate_keystream(self):
        keystream = ""
        for i in range(self.n):
            # Aggiungi il bit calcolato al keystream.
            keystream += str(next(self))
        return keystream


# Crea un'istanza della classe LFSR con il seed '10101010' e i taps [6, 3].
my_lfsr = LFSR(seed='10101010', taps=[6, 3],n=15)
# Genera una sequenza di 10 bit pseudocasuali.
keystream = my_lfsr.generate_keystream()
print(keystream)



