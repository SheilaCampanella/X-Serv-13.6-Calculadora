#!/usr/bin/python3

import sys

try:
    operando1 = float(sys.argv[2])
    operando2 = float(sys.argv[3])
except ValueError:
    sys.exit("Solo se permiten operandos float")

if sys.argv[1] == 'sumar':
    print(operando1 + operando2)

elif sys.argv[1] == 'restar':
    print(operando1 - operando2)

elif sys.argv[1] == 'multiplicar':
    print(operando1 * operando2)

elif sys.argv[1] == 'dividir':
    try:
        print(operando1 / operando2)
    except ZeroDivisionError:
        sys.exit("No se puede dividir entre cero")

