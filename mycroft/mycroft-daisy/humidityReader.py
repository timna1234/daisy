import smbus

bus = smbus.SMBus(1) 
DEVICE_ADDRESS = 0x04

class I2C_Humidity_Reader():
     
    def get_data(self):
        return bus.read_byte(DEVICE_ADDRESS)
        