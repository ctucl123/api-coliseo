import RPi.GPIO as GPIO
import time
class GpiosManager():
    def __init__(self):
        super().__init__()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.electroiman = 5
        self.semaforo = 27
        GPIO.setup(self.electroiman, GPIO.OUT)
        GPIO.setup(self.semaforo, GPIO.OUT)
        GPIO.setup(self.sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.output(self.semaforo,GPIO.LOW)
        GPIO.output(self.electroiman,GPIO.HIGH)

        
    def doorOpen(self):
        GPIO.output(self.electroiman, GPIO.LOW)  
        GPIO.output(self.semaforo, GPIO.HIGH) 
        return "puerta general abierta" 
    
    def doorClose(self):
        GPIO.output(self.electroiman, GPIO.HIGH)
        GPIO.output(self.semaforo, GPIO.LOW)
         
    def testArrow(self):
        GPIO.output(self.semaforo, GPIO.LOW)
        time.sleep(2)
        GPIO.output(self.semaforo, GPIO.HIGH)
        time.sleep(2)
        return 'Luz Led testeada con exito'
    
    def ReadSensor(self):
        return bool(GPIO.input(self.sensor))



   
    
    

        