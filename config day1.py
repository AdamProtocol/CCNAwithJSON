#config day 1
import json
import serial
import telnetlib
from Rivan_functions import *
import serial.tools.list_ports
import serial

import time
comlist = serial.tools.list_ports.comports()
com_num = ''
for i in comlist:
    com_num = str(i)[3:4]

def initserial(com):
    console = serial.Serial(
        port=f'COM{str(com)}',
        baudrate=9600,
        parity="N",
        stopbits=1,
        bytesize=8,
        timeout=8
    )
    return console



with open('devices.json','r') as f:
    buksan_file = json.load(f)

def config_it(monitor_num):
    main = initserial(com_num)
    dev_config = Ciscoconfig('11','LEAFSW')
    dev_config.initconfigdev(main,'pass')
    print(main.read_all())
    main.close()

config_it(com_num)
print('natapos na')




