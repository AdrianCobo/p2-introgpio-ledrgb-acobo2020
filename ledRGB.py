

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

    flag = False
    print("los colores disponibles para encender o apagar son: rojo,verde,azul,rosa,blanco,amarillo y azulClarito")
    print("si no funciona es por que has escrito mal el comando,vuelve a intentarlo o lee el read.me")
    while flag == False:
        accion_usuario = input("que accion quieres realizar (encender/apagar nombreColorMostradoAntriormente o salir) ")
        if accion_usuario == "encender rojo":
            encenderRojo()
        elif accion_usuario == "apagar rojo":
            apagar(rojoPin)

        elif accion_usuario == "encender verde":
            encenderVerde()
        elif accion_usuario == "apagar verde":
            apagar(verdePin)

        elif accion_usuario == "encender azul":
            encenderAzul()
        elif accion_usuario == "apagar azul":
            apagar(azulPin)

        if accion_usuario == "encender amarillo":
            encenderAmarillo()
        elif accion_usuario == "apagar amarillo":
            apagar(rojoPin)
            apagar(verdePin)

        elif accion_usuario == "encender rosa":
            encenderRosa()
        elif accion_usuario == "apagar rosa":
            apagar(rojoPin)
            apagar(azulPin)

        elif accion_usuario == "encender blanco":
            encenderBlanco()
        elif accion_usuario == "apagar blanco":
            apagar(rojoPin)
            apagar(azulPin)
            apagar(verdePin)
        elif accion_usuario == "encender azulClarito":
            encenderAzulClarito()
        elif accion_usuario == "apagar azulClarito":
            apagar(verdePin)
            apagar(azulPin)
        elif accion_usuario == "salir":
            flag = True
            GPIO.cleanup()
        time.sleep(1)

if __name__ == "__main__":
    main()