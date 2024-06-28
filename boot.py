# Complete project details at https://RandomNerdTutorials.com



from tiny32_v3 import tiny32_v3

try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'REPLACE_WITH_YOUR_SSID'
password = 'REPLACE_WITH_YOUR_PASSWORD'

# station = network.WLAN(network.STA_IF)

# station.active(True)
# station.connect(ssid, password)

# while station.isconnected() == False:
#   pass

# print('Connection successful')
# print(station.ifconfig())

tiny32_v3.header_print()
print("Info: boot.py ... runing")
tiny32_v3.Buzzer_beep(1)