import RPi.GPIO as GPIO
from time import sleep
from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)
Motor1A = 16
Motor1E = 22

def gpioSetup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(Motor1A,GPIO.OUT)
	GPIO.setup(Motor1E,GPIO.OUT)

def up():
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.LOW)
	sleep(1)
	GPIO.output(Motor1A,GPIO.LOW)

def down():   
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)
	sleep(2)
	GPIO.output(Motor1E,GPIO.LOW)

@app.route('/time-for-tea')
def timeForTea():	
	down()
	up()
	return render_template('done.html')

@app.route('/')
def hello_world():
	return render_template('welcome.html')

try:
	gpioSetup()
	up()

	if __name__ == '__main__':
		app.run(host='0.0.0.0')

	GPIO.cleanup()
except:
	GPIO.cleanup()
	raise
