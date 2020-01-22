import serial 

ser = serial.Serial(port= 'COM1', baudrate=9600,bytesize=serial.EIGHTBITS,timeout=2)

try:
    ser.isOpen()
except:
    print("error")
    exit()
if(ser.isOpen()):
    try:
        while(1):
            if(ser.inWaiting()>0):
                print (ser.readline())
            else:
                ser.write(b'1')
    except Exception as e:
        print (e)