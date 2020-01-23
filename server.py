import serial 

ser = serial.Serial(port= 'COM2', baudrate=9600)

print(ser.name)
ser.write(b'hello')

                                                                                                                                                                                                                                                                                                                                                                                               
while(True):

    print(ser.read(2))


