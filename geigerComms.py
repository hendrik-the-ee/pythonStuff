# retrieve data from geiger counter and put it up on the screen.
# keep in mind that the USB port may change

import serial

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600)
print ("serial port open: ", ser.isOpen)
print(ser.name)

while 1:
    out = ser.readline()
    print(out)
    
