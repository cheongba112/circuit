import RPi.GPIO as GPIO
import time

tpin = 16
epin = 18
max_dis = 220
timeout = max_dis * 60

def pulsein(pin, level, timeout):
    t0 = time.time()
    while GPIO.input(pin) != level:
        if (time.time() - t0) > timeout * 0.000001:
            return 0
    t0 = time.time()
    while GPIO.input(pin) == level:
        if (time.time() - t0) > timeout * 0.000001:
            return 0
    return (time.time() - t0) * 1000000

def getsonar():
    GPIO.output(tpin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(tpin, GPIO.LOW)
    pingtime = pulsein(epin, GPIO.HIGH, timeout)
    return pingtime * 0.017

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(tpin, GPIO.OUT)
    GPIO.setup(epin, GPIO.IN)
    try:
        while 1:
            dis = getsonar()
            print(dis)
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()

