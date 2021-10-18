

import time, sys
import RPi.GPIO as GPIO

rojoPin = 11
azulPin = 13
verdePin = 15


def encender(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def apagar(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def encenderRojo():
    encender(rojoPin)
    apagar(azulPin)
    apagar(verdePin)

def encenderVerde():
    encender(verdePin)
    apagar(azulPin)
    apagar(rojoPin)

def encenderAzul():
    encender(azulPin)
    apagar(verdePin)
    apagar(rojoPin)

def encenderRosa():
    encender(azulPin)
    encender(rojoPin)
    apagar(verdePin)

def encenderBlanco():
    encender(azulPin)
    encender(rojoPin)
    encender(verdePin)

def encenderAmarillo():
    encender(verdePin)
    encender(rojoPin)
    apagar(azulPin)

def encenderAzulClarito():
    GPIO.setmode(GPIO.BOARD)
    encender(verdePin)
    encender(azulPin)
    apagar(rojoPin)

def main():

    encenderRojo()
    input("Pulsa para tornar verde")
    encenderVerde()

    input("Pulsa para tornar azul")
    encenderAzul()

    input("Pulsa para tornar rosa")
    encenderRosa()

    input("Pulsa para tornar blanco")
    encenderBlanco()

    input("Pulsa para tornar amarillo")
    encenderAmarillo()

    input("Pulsa para tornar azulClarito")
    encenderAzulClarito()

    input("Pulsa para apagar")
    apagar(rojoPin)
    apagar(azulPin)
    apagar(verdePin)
    GPIO.cleanup()

if __name__ == "__main__":
    main()