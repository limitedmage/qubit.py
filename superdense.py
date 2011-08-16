'''
Superdense coding protocol simulator
Created by Juliana Pena
http://julianapena.com

Released freely under Ms-PL
http://www.opensource.org/licenses/ms-pl

Dependencies:
Python 2.7
Quantum bit simulator (qubit.py)
'''

from qubit import *

def superdense_coding():
    '''The superdense coding protocol
       This protocol will show how
       two classical bits can be
       stored in a single qubit'''

    print "=============================================="
    print "==========Superdense coding protocol=========="
    print "=============================================="
    print

    a = TwoQubit()
    print "Eve starts with two qubits in state", a

    print
    print "Eve prepares Bell state, first with Hadamard gate on first qubit:"

    a.hgate()
    print a

    print "and then with controlled Not gate on the two qubits:"

    a.cnot()
    print a

    print
    print "Eve sends one qubit to Alice and another to Bob."
    print

    print "Alice wants to encode two classical bits to send to Bob"
    print "with only her one qubit"
    print

    x = raw_input("First bit: ")
    while x not in ["0", "1"]:
        print "Wrong input (0 or 1 only)"
        x = raw_input("First bit: ")

    y = raw_input("Second bit: ")
    while y not in ["0", "1"]:
        print "Wrong input (0 or 1 only)"
        y = raw_input("Second bit: ")

    x = int(x)
    y = int(y)

    print
    if x == 0 and y == 0:
        print "For encoding 00, nothing is done (I gate is applied)"
    elif x == 0 and y == 1:
        print "For encoding 01, the X (NOT) gate is applied"
        a.xgate()
    elif x == 1 and y == 0:
        print "For encoding 10, the Z gate is applied"
        a.zgate()
    else:
        print "For encoding 11, the X and Z gates are applied"
        a.xgate().zgate()

    print a
    print

    print "Because Alice and Bob's qubits were entangled by Eve,"
    print "Alice's operations affect both, despite being far apart."

    print
    print "Alice sends her qubit to Bob. Now Bob has both original qubits."

    print
    print "Bob applies a reverse operation of Eve's original operation"

    print "First a controlled Not:"
    a.cnot()
    print a

    print "Then a Hadamard on the first Qubit:"
    a.hgate()
    print a

    print
    print "Finally, Bob measures the qubits in the computational basis."

    res = a.measure()
    print "The result of Bob's measurement is", res, ", Alice's two bits."

if __name__ == '__main__':
    superdense_coding()
