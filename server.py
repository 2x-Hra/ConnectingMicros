import serial 

ser = serial.Serial(port= 'COM2', baudrate=9600)

print(ser.name)
ser.write(b'hello')

                                                                                                                                                                                                                                                                                                                                                                                               
while(True):

    temp = str(ser.read(2))
    temp_list = list(temp)
    temp_list.pop(1)
    temp_list.pop(len(temp_list)-1)
    temp_list.pop(0)
    # print(temp_list)
    print(''.join(temp_list))
    

