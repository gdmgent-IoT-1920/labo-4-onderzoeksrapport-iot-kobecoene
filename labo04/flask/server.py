# import libraries
from flask import Flask, render_template, request
from sense_hat import SenseHat

# sensehat instantiëren
sense = SenseHat()

# flask server instantiëren
app = Flask(__name__)

sense_values = {
    'value': '#000000',
    'type': 'hex'
}

@app.route('/')
def index():
    return 'Hello World'

@app.route('/hello')
def hello():
    return 'You have reached the Pi of F-Rogers'

@app.route('/sensehat', methods=['GET', 'POST'])
def sensehat():
    if(request.method == 'POST'):
        sense_values['value'] = request.form['senseColor']
        def hex_to_rgb(value):
            value = value.lstrip('#')
            lv = len(value)
            return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
        color = hex_to_rgb(sense_values['value'])
        sense.clear(color)

		
    return render_template('sensehat.html.j2', sense_values = sense_values)

# server constants
host = '192.168.0.151'
port = 8080
if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)