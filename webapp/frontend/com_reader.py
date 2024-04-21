import serial
import threading
import random
import time

# Define global variables
#ser = serial.Serial("COM7", 115200, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
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
        
        new_data = integers

def fake_data():
    #while True:
    new_data.append([random.randint(1,140),random.randint(1,140),random.randint(1,140),random.randint(1,140)])
    
        #time.sleep(0.5)
def get_data():
    global new_data
    global all_data
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
#t1 = threading.Thread(target=fake_data)
#t1.start()