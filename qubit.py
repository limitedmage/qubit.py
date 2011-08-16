'''
Quantum bit simulator
Created by Juliana Pena
http://julianapena.com

Released freely under Ms-PL
http://www.opensource.org/licenses/ms-pl

Dependencies:
Python 2.7
'''

import math
import random

class Qubit:
    def __init__(self, a = 1, b = 0):
        '''Initialize a single qubit'''
        self.zero = complex(a)
        self.one  = complex(b)

    def xgate(self):
        '''Apply a NOT (X) gate'''
        self.zero, self.one = self.one, self.zero
        return self

    def zgate(self):
        '''Apply a Z gate'''
        self.one = -self.one

    def hgate(self):
        '''Apply a Hadamard gate'''
        a = self.zero
        b = self.one
        self.zero = a + b
        self.one = a - b
        self.normalize()
        return self

    def measure(self):
        '''Measure the qubit in the computational basis'''
        zeroprob = abs(self.zero) ** 2
        randomchoice = random.random()
        
        if randomchoice < zeroprob:
            self.zero = complex(1)
            self.one  = complex(0)
            return 0
        else:
            self.zero = complex(0)
            self.one  = complex(1)
            return 1

    def normalize(self):
        '''Normalize the qubit to a unit vector'''
        norm = (abs(self.zero) ** 2 + abs(self.one) ** 2) ** 0.5
        self.zero /= norm
        self.one /= norm
        return self

    def __repr__(self):
        return str(self.zero) + " |0> + " + str(self.one) + " |1>\n"

    
class TwoQubit:
    def __init__(self, a = 1, b = 0, c = 0, d = 0):
        '''Initialize a two-qubit entanglement'''
        self.zerozero = complex(a)
        self.zeroone  = complex(b)
        self.onezero  = complex(c)
        self.oneone   = complex(d)

    def cnot(self):
        '''Controlled NOT operation'''
        self.onezero, self.oneone = self.oneone, self.onezero
        return self

    def hgate(self):
        '''Perform Hadamard operation on first qubit'''
        a = self.zerozero
        b = self.zeroone
        c = self.onezero
        d = self.oneone

        self.zerozero = a + c
        self.zeroone  = b + d
        self.onezero  = a - c
        self.oneone   = b - d

        self.normalize()

        return self

    def xgate(self):
        '''Apply an X (NOT) gate to the first qubit'''
        a = self.zerozero
        b = self.zeroone
        c = self.onezero
        d = self.oneone

        self.zerozero = c
        self.zeroone  = d
        self.onezero  = a
        self.oneone   = b

        return self

    def zgate(self):
        '''Apply a Z gate on the first qubit'''
        self.onezero *= -1
        self.oneone  *= -1

        return self
    
    def normalize(self):
        '''Normalize the two-qubit entanglement to a unit vector'''
        norm = (abs(self.zerozero) ** 2 + abs(self.zeroone) ** 2 +
                abs(self.onezero) ** 2 + abs(self.oneone) ** 2) ** 0.5
        self.zerozero /= norm
        self.zeroone  /= norm
        self.onezero  /= norm
        self.oneone   /= norm
        return self

    def measure(self):
        '''Measure the two-qubit in the computational basis'''
        zerozeroprob = abs(self.zerozero) ** 2
        zerooneprob  = abs(self.zeroone)  ** 2
        onezeroprob  = abs(self.onezero)  ** 2
        randomchoice = random.random()
        
        if randomchoice < zerozeroprob:
            self.zerozero = complex(1)
            self.zeroone  = complex(0)
            self.onezero  = complex(0)
            self.oneone   = complex(0)
            return (0, 0)
        elif randomchoice < zerooneprob:
            self.zerozero = complex(0)
            self.zeroone  = complex(1)
            self.onezero  = complex(0)
            self.oneone   = complex(0)
            return (0, 1)
        elif randomchoice < onezeroprob:
            self.zerozero = complex(0)
            self.zeroone  = complex(0)
            self.onezero  = complex(1)
            self.oneone   = complex(0)
            return (1, 0)
        else:
            self.zerozero = complex(0)
            self.zeroone  = complex(0)
            self.onezero  = complex(0)
            self.oneone   = complex(1)
            return (1, 1)
        
    
    def __repr__(self):
        comp = [self.zerozero, self.zeroone, self.onezero, self.oneone]
        comp = [i.real if i.real == i else i for i in comp]
        comp = [str(i) for i in comp]
        comp = ["" if i == "1.0" else i for i in comp]

        ls = []
        if abs(self.zerozero) > 0:
            ls += [comp[0] + " |00>"] 
        if abs(self.zeroone)  > 0:
            ls += [comp[1] + " |01>"] 
        if abs(self.onezero)  > 0:
            ls += [comp[2]  + " |10>"] 
        if abs(self.oneone)   > 0:
            ls += [comp[3]   + " |11>"] 

        comp = " + ".join(ls)
        
        return comp


    
