import board
import adafruit_bme280.basic as adafruit_bme280

i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

print(f"Температура : {bme280.temperature:.1f} °C")
print(f"Влажност    : {bme280.relative_humidity:.1f} %")
print(f"Налягане    : {bme280.pressure:.1f} hPa")