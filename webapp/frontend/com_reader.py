import serial
import threading
import random
import time

# Define global variables
ser = None
try:
    ser = serial.Serial("COM3", 115200, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
except:
    print("Serial port not found")
    ser = None

all_data = []
new_data = []
terminate = False

# Start of function definitions
def receive_data():
    global new_data
    global terminate
    global ser
    
    if ser == None:
        print("Serial port not found")
        return
    
    while True:
        if terminate:
            break
        
        cc = ser.read(4)
        
        integers = []

        for byte in cc:
            integers.append(byte)
        
        integers[1]*=255


        print(integers)
        
        new_data = [integers]

def fake_data():
    global new_data
    #while True:
    new_data = [[random.randint(1,140),random.randint(1,140),random.randint(1,140),random.randint(1,140)]]
    
        #time.sleep(0.5)
def get_data():
    global new_data
    # global all_data
    #all_data.append(new_data)
    # ti ne smes belezit podatkov ampak sam nove posiljas da jaz lah 
    # izbiram zacetek pa konec rida ker drgač bo meru k ne bo nic
    #temp = new_data
    #new_data = []
    #if len(temp) < 1:
    #    return [[-1,-1,-1,-1]]

    # new_data = []
    # fake_data()
    # temp = new_data

    return new_data


# Start of main code
t1 = threading.Thread(target=receive_data)
t1.start()
print("Thread started")