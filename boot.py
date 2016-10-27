# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal
from machine import UART
from network import WLAN
from os import dupterm
from time import sleep_ms

# enable the UART on the USB-to-serial port
uart = UART(0, baudrate=115200)
# duplicate the terminal on the UART
dupterm(uart)
print('UART initialised!')

import settings

# login to the local network
print('Initialising WLAN in station mode...', end=' ')
wlan = WLAN(mode=WLAN.STA)
print('done.\nConnecting to WiFi network...', end='')
wlan.ifconfig(config='dhcp')
AUTH = (WLAN.WPA2, settings.wifiKey)
wlan.connect(ssid= settings.SSID, auth=AUTH)
while not wlan.isconnected():  
    sleep_ms(500)
    print('.', end='')
print(' done.\n')

# print
ip, mask, gateway, dns = wlan.ifconfig()
print('IP address: ', ip)
print('Netmask:    ', mask)
print('Gateway:    ', gateway)
print('DNS:        ', dns)

sleep_ms(1000)


