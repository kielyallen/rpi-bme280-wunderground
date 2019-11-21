# used with https://github.com/adafruit/Adafruit_Python_GPIO and https://github.com/adafruit/Adafruit_Python_BME280

import requests
import sys
import time
from Adafruit_BME280 import *

bme = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
# post to wunderground PWS
api_url = 'https://rtupdate.wunderground.com/weatherstation/updateweatherstation.php'
wun_station = sys.argv[1] # wunderground pws station name
wun_key = sys.argv[2] # wunderground pws station key
elevation = float(sys.argv[3]) # elevation above sea level in meters
pressure_cal = float(sys.argv[4]) # pressure calibration in pascals. leave set to 0 unless a calibrated reference is used.

def get_sensor_data():
        temperature = bme.read_temperature()
        humidity = bme.read_humidity()
        raw_pressure = (bme.read_pressure() + pressure_cal)
        dewpoint = temperature - ((100 - humidity) / 5) # may not be accurate with lower humidity values
        pressure_hpa = raw_pressure / 100
        pressure_sea_hpa = pressure_hpa*(1-(0.0065*elevation)/(temperature+(0.0065*elevation)+273.15))**-5.257
        return {
                'tempc': temperature,
                'tempf': (temperature * 1.8) + 32,
                'humidity': humidity,
                'pressure_pa': raw_pressure,
                'pressure_hpa': raw_pressure / 100,
                'pressure_inhg': raw_pressure * 0.00029530,
                'pressure_sea_hpa': pressure_sea_hpa,
                'pressure_sea_inhg': pressure_sea_hpa * 0.029530,
                'dewpointc': temperature - ((100 - humidity) / 5),
                'dewpointf': (dewpoint * 1.8) + 32
        }

def print_sensor_data(wx_data):
        print time.ctime()
        print ('''Temperature = {tempc:0.1f}C
Temperature = {tempf:0.1f}F
Humidity = {humidity:0.1f}%
Dew Point = {dewpointc:0.1f}C
Dew Point = {dewpointf:0.1f}F
Pressure = {pressure_pa:0.2f}Pa
Pressure = {pressure_hpa:0.0f}hPa
Pressure = {pressure_inhg:0.2f}inHg
Sea Level Pressure = {pressure_sea_hpa:0.0f}hPa
Sea Level Pressure = {pressure_sea_inhg:0.2f}inHg'''.format(**wx_data))

def wun_upload(wx_data):
        parameters = {'tempf':wx_data['tempf'],
                      'baromin':wx_data['pressure_sea_inhg'],
                      'humidity':wx_data['humidity'],
                      'dewptf':wx_data['dewpointf'],
                      'action':'updateraw',
                      'dateutc':'now'}

        try:
            r = requests.get(api_url + '?ID=' + wun_station + '&PASSWORD=' + wun_key, params=parameters, timeout=15)
            r.raise_for_status()
            print r.status_code
            print r.text
        except requests.exceptions.HTTPError as eh:
            print eh
        except requests.exceptions.ConnectionError as ec:
            print ec
        except requests.exceptions.Timeout as et:
            print et
        time.sleep(60)

while True:
        wx_data = get_sensor_data()
        print_sensor_data(wx_data)
        wun_upload(wx_data)
