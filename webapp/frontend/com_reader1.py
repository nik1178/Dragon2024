import serial
import threading
import random
import time
import keyboard

# Define global variables
ser = serial.Serial("COM8", 115200, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
all_data = []
new_data = []
terminate = False

# Start of function definitions
def receive_data():
    global new_data
    global terminate
    
    while True:
        if terminate:
            break
        
        cc = ser.read(5)
        
        integers = []

        for byte in cc:
            integers.append(byte)
        
        new_data.append(integers)

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
    for i,x in enumerate(temp):
        if len(x) != 4:
            temp[i] = [-1,-1,-1,-1]
        
    return temp


# Start of main code
t1 = threading.Thread(target=receive_data)
t1.start()

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            terminate = True
            exit()
    except:
        break  # if user pressed a key other than the given key the loop will break