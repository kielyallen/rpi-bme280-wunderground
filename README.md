# rpi-sensors
Raspberry Pi Weather/Atmospheric Sensors


**Bosch BME280 Temp/Humidity/Pressure Sensor**\
**5V Version** (Check if 5V or 3V Sensor!!)

*Raspberry Pi Zero W* Pinout:\
5v to 5v (Pin 2)\
Ground to Ground (Pin 6)\
SDA to Pin 3 (GPIO 2)\
SCL to Pin 5 (GPIO 3)

Using Adafruit BME280 driver: https://github.com/adafruit/Adafruit_Python_BME280

**Notes:** i2c address was 0x76 for 5V version, Adafruit driver looks for 0x77.\

Line 30 in Adafruit_BME280.py (included in above BME280 driver) was changed from:\
`BME280_I2CADDR = 0x77`\
to\
`BME280_I2CADDR = 0x76`

BME280 Datasheet: https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BME280-DS002.pdf
