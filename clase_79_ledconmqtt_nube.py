import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

def conectado(cliente,userdata,flags,rc):
    if rc == 0:
        print("Cliente conectado OK")
        cliente.subscribe("demo2023")
    else:
        print("Cliente no se pudo conectar")
        
def receptor(cliente,userdata,mensaje):
    print(mensaje.payload)
    men = mensaje.payload.decode() ##porque nos interesa solo letras
    print(men)
    if men == "a":
        GPIO.output(2,GPIO.HIGH)
    elif men == "b":
        GPIO.output(2,GPIO.LOW)
        
        
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

cliente = mqtt.Client("eugenio09")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
cliente.connect ("node02.myqtthub.com",1883)
cliente.username_pw_set(username="eugenio",password="1234")
 
cliente.on_connect = conectado
cliente.on_message = receptor

cliente.loop_forever()
print("Fin de Programa")	