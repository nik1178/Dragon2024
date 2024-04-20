import serial
import threading
import random
import time

# Define global variables
# ser = serial.Serial("COM7", 115200, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
all_data = []
new_data = []

# Start of function definitions
def receive_data():
    global new_data
    
    while True:
        ser.write(b'1')
        cc=str(ser.readline())
        print(cc)
        if len(cc) < 1:
            continue
        
        cc = cc[2:-2]
        
        split_table = cc.split("\\")
        if len(split_table) < 2:
            continue
        
        print(split_table)
        for i,x in enumerate(split_table):
            if len(x) < 1:
                split_table.pop(i)
                continue
            if x[0] == 'x':
                split_table[i] = int(x[1:], 16)
            else:
                split_table[i] = int(x)
        
        data = []
        for i,x in enumerate(split_table):
            data.append(x)
        
        new_data.append(data)
        
        print(data)

def fake_data():
    while True:
        new_data.append([random.randint(1,140),random.randint(1,140),random.randint(1,140),random.randint(1,140)])
        time.sleep(1)
        print(new_data)

def get_data():
    global new_data
    global all_data
    all_data.append(new_data)
    temp = new_data
    new_data = []
    if len(temp) < 1:
        return [[-1,-1,-1,-1]]
    return temp


# Start of main code
t1 = threading.Thread(target=fake_data)
t1.start()