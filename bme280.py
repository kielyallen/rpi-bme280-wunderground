# used with https://github.com/adafruit/Adafruit_Python_GPIO and https://github.com/adafruit/Adafruit_Python_BME280

import time
from Adafruit_BME280 import *

bme = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
elevation = 91.44 # in meters

while True:
        temperature = bme.read_temperature()
        humidity = bme.read_humidity()
        pressure = bme.read_pressure()
        fah = (temperature  * 1.8) + 32
        hpa = pressure / 100
        inHg = pressure * 0.00029530
        seaLevelh = hpa*(1-(0.0065*elevation)/(temperature+(0.0065*elevation)+273.15))**-5.257 
        seaLeveli = seaLevelh * 0.029530

        print 'Temperature = {:0.1f}F'.format(fah)
        print 'Temperature = {:0.1f}C'.format(temperature)
        print 'Humidity = {:0.1f}%'.format(humidity)
        print 'Pressure = {:0.2f}Pa'.format(pressure)
        print 'Pressure = {:0.0f}hPa'.format(hpa)
        print 'Pressure = {:0.2f}inHg'.format(inHg)
        print 'Sea Level Pressure = {:0.0f}hPa'.format(seaLevelh)
        print 'Sea Level Pressure = {:0.4f}inHg'.format(seaLeveli)
        print '----------------------'
        time.sleep(15)
