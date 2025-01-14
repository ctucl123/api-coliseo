from flask import Flask, render_template, request,jsonify
import threading
from rs232 import rs232Comunication
from gpiosManager import GpiosManager
from MecanismLogic import Manager
from database.SqliteManager import SqliteManager

#from audioManager import AudioManager
#version 3.6
app = Flask(__name__)
stop_event = threading.Event()

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        operation = request.form.get('operation')
        if operation == 'ReadSensor':
            estado = gpios.ReadSensor()
            result = f'sensor: {estado}'
        elif operation == 'generatePass':
            manager.generatePass()
            result = f'Pase generado'
        elif operation == 'TestLuzLed':
            result = gpios.testArrow()
        else:
            result = f'Error Operacion No existente'
    return render_template('home.html', result=result)

@app.route('/api/rs232', methods=['GET', 'POST'])
def rs232_Api():
    if request.method == 'GET':
        operation = request.get_json()
        if operation['operation'] == "validations":
            return  jsonify({"validations":rs232.n_validations})
        return
    
@app.route("/datos")
def datos():
    return rs232.getData()

if __name__ == "__main__":
    rs232 = rs232Comunication( stop_event=stop_event,com='/dev/ttyACM0')
    manager = Manager(stop_event=stop_event,rs232=rs232)
    gpios = GpiosManager()
    rs232.start()
    manager.start()

    try:
        app.run(host='0.0.0.0', port=5000,use_reloader=False)
    finally:
        stop_event.set()
        rs232.join()
        manager.join()
        print("programa terminado!")

#'/dev/ttyUSB0'
#'/dev/ttyACM0'