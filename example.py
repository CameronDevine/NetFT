from __future__ import print_function
import NetFT
sensor = NetFT.NetFT('192.168.0.10')
print(sensor.getMeasurement())
sensor.tare()
print(sensor.getMeasurement())
