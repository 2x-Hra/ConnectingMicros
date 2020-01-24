import serial 
import time

ser = serial.Serial(port= 'COM2', baudrate=9600)

print(ser.name)
while(True):

    temp = input("000 Or MOTOR speed :")
    ser.write(str.encode(temp))
    if(temp == "000"):
        temp_analog = str(ser.read(2))
        temp_list = list(temp_analog)
        temp_list.pop(1)
        temp_list.pop(len(temp_list)-1)
        temp_list.pop(0)
        print(''.join(temp_list))
  
   


# while(True):
#     ser.write(str.encode("100"))
#     time.sleep(0.6)
    
    # temp = str(ser.read(2))
    # temp_list = list(temp)
    # temp_list.pop(1)
    # temp_list.pop(len(temp_list)-1)
    # temp_list.pop(0)
    # # print(temp_list)
    # print(''.join(temp_list))
    # time.sleep(0.8)
    

