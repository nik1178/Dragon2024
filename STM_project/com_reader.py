import serial
import threading

# Define global variables
ser = serial.Serial("COM7", 115200, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
all_data = []
new_data = []

# Start of function definitions
def receive_data():
    while True:
        ser.write(b'1')
        cc=str(ser.readline())
        if len(cc) < 1:
            continue
        
        split_table = cc.split("\\x")
        split_table.pop(0)
        
        for i,_ in enumerate(split_table):
            split_table[i] = split_table[i].replace("\\", "")
            split_table[i] = split_table[i].replace("t", "")
            split_table[i] = split_table[i].replace("'", "")
        
        data = []
        for i,x in enumerate(split_table):
            data.append(int(x, 16))
        
        print(data)
def fake_data():
    while True:
        cc="b'\\x05\\xc7\\x22'\\\\t"
        if len(cc) < 1:
            continue
        
        split_table = cc.split("\\x")
        split_table.pop(0)
        
        for i,_ in enumerate(split_table):
            split_table[i] = split_table[i].replace("\\", "")
            split_table[i] = split_table[i].replace("t", "")
            split_table[i] = split_table[i].replace("'", "")
        
        data = []
        for i,x in enumerate(split_table):
            data.append(int(x, 16))

def get_data():
    all_data.append(new_data)
    temp = new_data
    new_data = []
    return temp


# Start of main code
t1 = threading.Thread(target=receive_data)
t1.start()