import time
import board
from analogio import AnalogIn 
import pwmio  

analog_in = AnalogIn(board.A2) #potentionmeter pin
pin_out = pwmio.PWMOut(board.D8,duty_cycle=65535,frequency=5000)

print("Starting up...")

while True:

    sensor_value = analog_in.value
    print("sensor value: ", sensor_value)

    pin_out.duty_cycle = sensor_value

    time.sleep(0.15)


  