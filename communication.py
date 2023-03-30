import random
import GNSS
import serial
import serial.tools.list_ports
import time
from pynmeagps import NMEAReader

gnss = GNSS.GNSS_data()
ilatitude = 27.7006
ilongitude = 85.3119
random_gps = []


class Communication:
    portName = ''
    dummyPlug = False
    ports = serial.tools.list_ports.comports()

    ser = serial.Serial()

    def __init__(self):
        # self.baudrate = 115200
        # self.portName = input("Write serial port name : ")
        if serial.Serial() is not open:
            try:
                # self.ser = serial.Serial(self.portName, self.baudrate)
                self.ser.flushInput()
                self.ser.flushOutput()
                # self.ser.write("get")
                # sleep(1) for 100 millisecond delay
                # 100ms dely
                time.sleep(.1)
            except serial.serialutil.SerialException:
                # print("Can't open : ", self.portName)
                self.dummyPlug = True
                print("Dummy mode activated")
        else:
            print("error")

    def close(self):
        if self.ser.isOpen():
            self.ser.close()
        else:
            print(self.portName, " it's already closed")

    def getData(self):
        #gps_array = gnss.get_gpsdata()
        value_chain = [0] + random.sample(range(0, 500), 1) + \
                      [random.getrandbits(1)] + random.sample(range(0, 50), 8)  + random.sample(
            range(0, 50), 10)
        # print(value_chain)
        #return value_chain,gps_array
        return value_chain 

    def isOpen(self):
        return self.ser.isOpen()


