from gpiosManager import GpiosManager
import threading
import time
import subprocess

#version 1.1

doors =  GpiosManager()
def timer(target_time):
    if doors.ReadSensor() == True:
        doors.doorOpen()
        inicio = time.time()
        while time.time() - inicio < 10:
            if doors.ReadSensor() == False:
                timeaux = time.time()
                while doors.ReadSensor() == False:
                    time.sleep(0.1)
                    if time.time() - timeaux >= 10:
                        doors.doorClose()
                        break
                doors.doorClose() 
                break


class Manager(threading.Thread):
    def __init__(self,rs232, stop_event):
        super().__init__()
        self.rs232 = rs232
        self.stop_event = stop_event
        self.time_door = 10     
        self.activatePass = 0
        self.specialPass = 0
    def run(self):
        while not self.stop_event.is_set():
            with self.rs232.lock:
                if self.activatePass >0:
                    temporizador_thread = threading.Thread(target=timer,args=(self.time_door))
                    temporizador_thread.start()
                    aux_pass =  self.activatePass - 1
                    if aux_pass < 0:
                        self.activatePass = 0
                    else:
                        self.activatePass = aux_pass
                    temporizador_thread.join()
            time.sleep(0.1)

    def generatePass(self):
        self.activatePass += 1


    
    

    
