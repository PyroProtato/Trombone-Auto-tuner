import serial
import time


try:
    ser = serial.Serial(
        port='COM6',        # Replace with your port
        baudrate=9600,
        bytesize=8,
        parity='N',
        stopbits=1,
        timeout=1
    )
    print(f"Connected to {ser.name}") 
    time.sleep(2)
    

except serial.SerialException as e:
    print(f"Error: {e}")




ser.write(b'out\n')

time.sleep(2)

ser.write(b"in\n")

time.sleep(2)

ser.write(b'out\n')

time.sleep(2)

ser.write(b"stop\n")

