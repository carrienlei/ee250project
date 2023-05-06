from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan

dht_sensor_port = 7 # connect the DHt sensor to port 7. This is for the GrovePi Temperature/Humidity Sensor.
dht_sensor_type = 0 # use 0 for the blue-colored sensor and 1 for the white-colored sensor. This is for the RGB LCD Display.

setRGB(0,255,0)

while True:
    try:
        [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
        print("temp =", temp, "C\thumidity =", hum,"%")

		# check if we have nans
		# if so, then raise a type error exception
        if isnan(temp) is True or isnan(hum) is True:
            raise TypeError('nan error')

        t = str(temp)
        h = str(hum)

        # instead of inserting a bunch of whitespace, we can just insert a \n
        # we're ensuring that if we get some strange strings on one line, the 2nd one won't be affected
        setText_norefresh("Temp:" + t + "C\n" + "Humidity :" + h + "%")
		
        if (temp>20):
            print ("Hot\n")
            print ("Men, wear loose shorts, denim shorts, T-shirts, tank tops, sunglasses, tropical shirts, caps, sombreros, bucket hats, denim jackets, cardigans, light jeans\n")
            print ("Women, wear skirts, crop tops, sundresses, sunglasses, bucket hats, caps, tank tops, swimwear, sandals, denim jackets, cardigans, light jeans, denim shorts\n")
            print ("Make sure you stay hydrate and have sunscreen on.\n\n")
            setRGB(255,0,0)
        else:
            print ("Cold\n")
            print ("Men, wear coats, jackets, bombers, parkas, jeans and warm pants, boots, scarves, beanies, gloves, and hoodies\n")
            print ("Women, wear coats, jackets, bombers, parkas, jeans and warm pants, boots, scarves, beanies, gloves, and hoodies\n")
            print ("Make sure you stay warm, or else you'll freeze to death.\n\n")
            setRGB(0,0,255)
	

    except (IOError, TypeError) as e:
        print(str(e))
	# 	# and since we got a type error
	# 	# then reset the LCD's text
        setText("")

    except KeyboardInterrupt as e:
        print(str(e))
	# since we're exiting the program
		# it's better to leave the LCD with a blank text
	# 	setText("")
	# 	break

	# wait some time before re-updating the LCD
    sleep(1)
