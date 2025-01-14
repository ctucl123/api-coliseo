import RPi.GPIO as GPIO
import time
class GpiosManager():
    def __init__(self):
        super().__init__()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.electroiman = 21
        self.semaforo = 20
        self.cruz_roja = 16
        self.flecha_verde = 12
        #configuraciones de salidas y entradas
        GPIO.setup(self.electroiman, GPIO.OUT)
        GPIO.setup(self.semaforo, GPIO.OUT)
        GPIO.setup(self.cruz_roja, GPIO.OUT)
        GPIO.setup(self.flecha_verde, GPIO.OUT)
        GPIO.setup(self.sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #valores iniciales
        GPIO.output(self.semaforo,GPIO.HIGH)
        GPIO.output(self.flecha_verde, GPIO.HIGH)
        GPIO.output(self.electroiman,GPIO.LOW)
        GPIO.output(self.cruz_roja, GPIO.LOW)

        
    def doorOpen(self):
        GPIO.output(self.electroiman, GPIO.HIGH)  
        GPIO.output(self.semaforo, GPIO.LOW)
        GPIO.output(self.flecha_verde, GPIO.LOW)
        GPIO.output(self.cruz_roja, GPIO.HIGH)
        return "puerta general abierta" 
    
    def doorClose(self):
        GPIO.output(self.electroiman, GPIO.LOW)  
        GPIO.output(self.semaforo, GPIO.HIGH)
        GPIO.output(self.flecha_verde, GPIO.HIGH)
        GPIO.output(self.cruz_roja, GPIO.LOW)
         
    def testArrow(self):
        GPIO.output(self.semaforo, GPIO.LOW)
        time.sleep(2)
        GPIO.output(self.semaforo, GPIO.HIGH)
        time.sleep(2)
        return 'Luz Led testeada con exito'
    
    def ReadSensor(self):
        return bool(GPIO.input(self.sensor))



   
    
    

        