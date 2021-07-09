import time
import napalm
from netmiko import ConnectHandler

user = 'myUser'
passwd = 'MyStrongPassword'

def connect(host, device_type,  attempts=10, timeout=1):
    driver = napalm.get_network_driver(device_type)
    device = driver(hostname=host, username=user, password=passwd)

    for _ in range(attempts):
        try:
            device.open()
            return device
        except:
            time.sleep(timeout)

    return False

def featch_serial(host):
    cisco = {
                'device_type': 'cisco_ios',
                'host': host,
                'username': 'myUser',
                'password': 'MyStrongPassword',
                'secret': 'MyStrongPassword',
            }
    net_connect = ConnectHandler(**cisco)
    net_connect.enable()
    info = net_connect.send_command('show version | include ID').split()
    net_connect.exit_enable_mode()
    net_connect.disconnect()
    return info[3]

            
def getGolden(host):
    for _ in range(10):
        try:
            cisco = {
                'device_type': 'cisco_ios',
                'host': host,
                'username': 'MyUser',
                'password': 'MyStrongPassword',
                'secret': 'MyStrongPassword',
            }
            net_connect = ConnectHandler(**cisco)
            net_connect.enable()
            net_connect.send_command_timing("copy tftp://172.16.100.10/golden.cfg startup-config")
            net_connect.exit_enable_mode()
            net_connect.disconnect()
            return True
        except:
            time.sleep(1)
    return
def reboot(host):
     cisco = {
     'device_type': 'cisco_ios',
     'ip': host,
     'username': user,
     'password': passwd,
     }

     net_connect = ConnectHandler(**cisco)
     net_connect.send_command_timing(command_string="reload", cmd_verify=True)
     net_connect.send_command_timing("\n")
     net_connect.disconnect()
     return None
