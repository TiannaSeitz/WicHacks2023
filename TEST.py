import RPi.GPIO as GPIO
import time

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)

    pin_number = 17
    GPIO.setup(pin_number, GPIO.IN)

    pin_state = GPIO.input(pin_number)

    signal = 0

    try:
        while signal == 0:
            if GPIO.input(pin_number):
                time.sleep(0.026)
                if GPIO.input(pin_number):
                    time.sleep(0.026)
                    if GPIO.input(pin_number):
                        signal = 3
                    else:
                        signal = 2
                else:
                    signal = 1
                print(signal)
                
    except KeyboardInterrupt:
        GPIO.cleanup()

    