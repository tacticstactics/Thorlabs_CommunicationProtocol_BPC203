from struct import pack,unpack
import serial
import time

#Basic Python APT/Kinesis Command Protocol Example using BPC203 and DRV001 in Channel 1
#Tested in Anaconda dsitrbution of Python 2.7 and virtual environment of Python 3.6
#Command Protol PDF can be found https://www.thorlabs.com/Software/Motion%20Control/APT_Communications_Protocol.pdf
#Pyserial is a not a native module installed within python and may need to be installed if not already

#Port Settings
baud_rate = 115200
data_bits = 8
stop_bits = 1
Parity = serial.PARITY_NONE

#Controller's Port and Channel
COM_Port = 'COM3' #Change to preferred
Channell = int(1)
Channel2 = int(2)
Channel3 = int(3)


#Device_Unit_SF = 819200. #pg 34 of protocal PDF (as of Issue 23)
destination1 = 0x21 #Destination byte; 0x21 for channel 1, 0x22 for channel 2, 0x23 for channel 3
destination2 = 0x22 #Destination byte; 0x21 for channel 1, 0x22 for channel 2, 0x23 for channel 3

source = 0x01 #Source byte

#Create Serial Object
BPC203 = serial.Serial(port =COM_Port, baudrate=baud_rate, bytesize=data_bits, parity=Parity, stopbits=stop_bits,timeout=0.1)

#MGMSG_MOD_IDENTIFY
BPC203.write(pack('<HBBBB', 0x0223, 0x01, 0x00, 0x11, source))

print('-----')
print('MGMSG_MOD_IDENTIFY')
time.sleep(3.0)

#MGMSG_MOD_IDENTIFY
BPC203.write(pack('<HBBBB', 0x0223, 0x02, 0x00, 0x11, source))

print('-----')
print('MGMSG_MOD_IDENTIFY')
time.sleep(1.0)

#MGMSG_MOD_IDENTIFY
BPC203.write(pack('<HBBBB', 0x0223, 0x03, 0x00, 0x11, source))

print('-----')
print('MGMSG_MOD_IDENTIFY')
time.sleep(1.0)




#MGMSG_MOD_SET_CHANENABLESTATE

BPC203.write(pack('<HBBBB', 0x0210, 0x01, 0x01, 0x11, source))
print('-----')
print('MGMSG_MOD_SET_CHANENABLESTATE')
time.sleep(1.0)


#MGMSG_PZ_SET_OUTPUTVOLTS
doutputvoltage = int(100.0)

BPC203.write(pack('<HBBBBHH', 0x0643, 0x04, 0x00, destination1|0x80, source, Channell, doutputvoltage))

#BPC203.write(pack('<HBBBBBBBB', 0x0643, 0x04, 0x00, destination|0x80, source, 0x01,0x00, 0x11, 0x11))

print('-----')
print('MGMSG_PZ_SET_OUTPUTVOLTS')
time.sleep(1.0)



#MGMSG_MOD_SET_CHANENABLESTATE
#10 / 02 / Chan Indent / Enable State / d /s
BPC203.write(pack('<HBBBB', 0x0210, 0x02, 0x01, 0x11, source))
print('-----')
print('MGMSG_MOD_SET_CHANENABLESTATE')
time.sleep(1.0)


#MGMSG_PZ_SET_OUTPUTVOLTS
doutputvoltage2 = int(200.0)

#BPC203.write(pack('<HBBBBHH', 0x0643, 0x04, 0x00, destination|0x80, source, Channel2, doutputvoltage2))

BPC203.write(pack('<HBBBBBBH', 0x0643, 0x04, 0x00, destination2|0x80, source, 0x02,0x00, doutputvoltage2))

print('-----')
print('MGMSG_PZ_SET_OUTPUTVOLTS')
time.sleep(1.0)


BPC203.close()
del BPC203
