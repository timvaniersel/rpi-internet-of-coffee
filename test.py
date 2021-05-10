import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!")

GPIO.setmode(GPIO.BOARD) # count the pins
GPIO.setwarnings(True) # We are testing right?

IN1 = 3 #ONOFF
IN2 = 5 #1xespresso
IN3 = 7 #2xespresso
IN4 = 11 #1xCoffee
IN5 = 13 #2xCoffee

def relay_init():
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN3, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN4, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN5, GPIO.OUT, initial=GPIO.HIGH)

def touch_button(pin):
    GPIO.output(pin, GPIO.LOW)
    print("A virtual button has been touched")
    time.sleep(0.5)
    GPIO.output(pin, GPIO.HIGH)


def touch_onoff():
    print("virtual touched ON/OFF button")
    touch_button(IN1)

def touch_espresso_1():
    print("virtual touched on espresso")
    touch_button(IN2)

def touch_espresso_2():
    print("virtual touched on espresso 2")
    touch_button(IN3)

def touch_coffee_1():
    print("virtual touched on coffee")
    touch_button(IN4)

def touch_coffee_2():
    print("virtual touched on coffee 2")
    touch_button(IN5)

    
relay_init()

GPIO.cleanup()
