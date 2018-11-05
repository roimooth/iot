import dht11
import RPi.GPIO as GPIO
import time

# Define GPIO to LCD mapping
Temp_sensor=14

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
instance = dht11.DHT11(pin = Temp_sensor)

while True:
    #get DHT11 sensor value
    result = instance.read()
    if result.is_valid():
        print("temp:"+str(result.temperature)+" C") #「lcd_string」を「print」に置き換えて、第2引数を削除した
        print("humid:"+str(result.humidity)+"%") #「lcd_string」を「print」に置き換えて、第2引数を削除した
        time.sleep(3) # 3 second delay
