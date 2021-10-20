# P2-Intropio-LEDRGB

## (CC-BY-NC-SA) Adrián Cobo Merino

El objetivo de este esta práctica es tener la primera toma de contacto con gpio y aprender a controlar un led rgb.

Algo que me ha parecido interesante el que al tener nuestro led la polaridad cambiada, para encender el led habia que "apagarlo" y viceversa
poniendo en alto la señal para apagar y en bajo para encender.
```python
def encender(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def apagar(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
```
Si quieres ver un video de demostracion, pulsa [aqui](https://drive.google.com/file/d/1Yw4JBJx-mFUy4UtezkkxtjzKz3q6Hydd/view?usp=sharing).
En el video podemos ver como como cambian los colores del led rgb.

Preguntas frecuentes:.

Pregunta: estoy metiendo el comando pero no hace nada.

respuesta:.
Seguramente estes metiendo mal el comando. Ejemplos de comando correctos: salir, apagar verde, encender azul,encender azulClarito.

Tienes que escribir los colores talcual te los indica al cargar el programa

Para cualquier duda: <a.cobo.2020@alumos.urjc.es>
