# rpi-bme280-wunderground
Raspberry Pi Bosch BME 280 Wunderground PWS Uploader


## Bosch BME280 Temp/Humidity/Pressure Sensor
**5V Version** (Check if 5V or 3V Sensor!!)

*Raspberry Pi Zero W* BME280 Pinout:\
5v to 5v (Pin 2)\
Ground to Ground (Pin 6)\
SDA to Pin 3 (GPIO 2)\
SCL to Pin 5 (GPIO 3)

Using Adafruit BME280 driver: https://github.com/adafruit/Adafruit_Python_BME280

**Notes:** i2c address was 0x76 for 5V version, Adafruit driver looks for 0x77.

Before running `python setup.py install` to begin the Adafruit driver installation, line 30 in Adafruit_BME280.py (included in above BME280 driver) was changed from:\
`BME280_I2CADDR = 0x77`\
to\
`BME280_I2CADDR = 0x76`

BME280 Datasheet: https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BME280-DS002.pdf

## Usage

`python bme280_wunderground.py <PWS Station Name> <PWS Station Key> <Elevation in Meters> <Pressure Calibration [0 is default, can be left blank]>`

## Output Example
`Thu Nov 21 00:36:12 2019`\
`Temperature = 5.7C`\
`Temperature = 42.2F`\
`Humidity = 79.4%`\
`Dew Point = 1.6C`\
`Dew Point = 34.8F`\
`Pressure = 100657.30Pa`\
`Pressure = 1007hPa`\
`Pressure = 29.72inHg`\
`Sea Level Pressure = 1018hPa`\
`Sea Level Pressure = 30.06inHg`\
`200`\
`success`
