import time
import digitalio
import board                                        

pi = digitalio.DigitalInOut(board.D7)
pi.direction = digitalio.Direction.INPUT
pi.pull = digitalio.Pull.UP
while True:
    print("pi value = ",pi.value, " ", time.monotonic())
    time.sleep(0.1)
