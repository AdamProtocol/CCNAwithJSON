#Rivan CCNA functions

class Ciscoconfig:
    def __init__(self,monitor_num,device_name):
        self.monitor_num = monitor_num
        self.device_name = device_name

    def checkmode(self,main):
    	pass


    def initconfigdev(self,main,passw):
        command = [
            b'enable \n',
            b'configure terminal \n',
            b'Hostname ' +self.device_name.encode('utf-8')+str(self.monitor_num).encode('utf-8')+b'\n',
            b'enable secret '+passw.encode('utf-8') + b'\n',
            b'service password-encryption \n',
            b'no logging console \n',
            b'no ip domain-lookup \n',
            b'line console 0  \n',
            b'password ' +passw.encode('utf-8') +b'\n',
            b'login \n',
            b'exec-timeout 0 0 \n',
            b'line vty 0 14 \n',
            b'password ' + passw.encode('utf-8') + b'\n',
            b'login \n'
            b'exec-timeout 0 0 \n'
        ]

        for i in command:
            main.write(i)

        print('Initialized!')