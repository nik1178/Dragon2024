import serial
import threading
import random
import time

# Define global variables
ser = serial.Serial("COM7", 115200, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
all_data = []
new_data = []

# Start of function definitions
def receive_data():
    global new_data
    
    while True:
        ser.write(b'1')
        cc = ser.readline()
        print(cc)
        if len(cc) < 1:
            continue
        
        temp = int
        

def fake_data():
    while True:
        new_data.append([random.randint(1,140),random.randint(1,140),random.randint(1,140),random.randint(1,140)])
        time.sleep(1)

def get_data():
    global new_data
    global all_data
    all_data.append(new_data)
    temp = new_data
    new_data = []
    if len(temp) < 1:
        return [[-1,-1,-1,-1]]
    else if len(temp[0]) < 1:
        return [[-1,-1,-1,-1]]
    return temp


# Start of main code
t1 = threading.Thread(target=receive_data)
t1.start()