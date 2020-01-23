import serial 

ser = serial.Serial(port= 'COM1', baudrate=9600)

print(ser.name)
ser.write(b'hello')

print(ser.is_open)