from datetime import datetime
import time
import os
import sys
import traceback

import bme680

from PIL import Image
import ST7789 as ST7789

def main():

    try:
        sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
    except Exception as e:
        # print(e)
        traceback.print_exc(file=sys.stdout)
        print('Could not configure the sensor. Exiting...')
        exit(1)

    print("""
    image.py - Display an image on the LCD.
    If you're using Breakout Garden, plug the 1.3" LCD (SPI)
    breakout into the front slot.
    """)

    if len(sys.argv) < 2:
        print("Usage: {} <image_file>".format(sys.argv[0]))
        sys.exit(1)

    image_file = sys.argv[1]

    # Create ST7789 LCD display class.
    disp = ST7789.ST7789(
        port=0,
        cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
        dc=9,
        backlight=19,               # 18 for back BG slot, 19 for front BG slot.
        spi_speed_hz=80 * 1000 * 1000
    )

    WIDTH = disp.width
    HEIGHT = disp.height

    # Initialize display.
    disp.begin()

    # Load an image.
    print('Loading image: {}...'.format(image_file))
    image = Image.open(image_file)

    # Resize the image
    image = image.resize((WIDTH, HEIGHT))

    # Draw the image on the display hardware.
    print('Drawing image')

    disp.display(image)




if __name__ == "__main__":
    main()