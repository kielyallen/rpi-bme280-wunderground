# rpi-sensors
Raspberry Pi Weather/Atmospheric Sensors


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

## Configuration

Replace the value for`elevation = 91.44` in bme280.py with your sensor's height above sea level in meters.

## Usage

`python bme280.py`

## Output Example
`Temperature = 40.6F`\
`Temperature = 4.8C`\
`Humidity = 31.4%`\
`Dew Point = -8.9C`\
`Dew Point = 16.0F`\
`Pressure = 102060.95Pa`\
`Pressure = 1021hPa`\
`Pressure = 30.14inHg`\
`Sea Level Pressure = 1032hPa`\
`Sea Level Pressure = 30.48inHg`\
`----------------------`
