from datetime import datetime
import time

from PIL import Image, ImageDraw, ImageFont
import ST7789 as ST7789

from outside import Outside
from inside import Inside
from IAQ import IAQ
from bar import AQ_Bar

SLEEP = 5   # seconds

def main():
    print('Initializing.')


    print('Initializing data sources')
    inside = Inside()
    outside = Outside()


    print('Initializing the display')
    disp = ST7789.ST7789(
        port=0,
        cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
        dc=9,
        backlight=19,               # 18 for back BG slot, 19 for front BG slot.
        spi_speed_hz=80 * 1000 * 1000
    )
    WIDTH = disp.width
    HEIGHT = disp.height
    disp.begin()


    print('Loading background image')
    image_file = 'background/bg.png'
    image = Image.open(image_file)


    print('Initializing drawing component')
    draw = ImageDraw.Draw(image)
    # TODO: can maybe get a custom better looking font
    font = ImageFont.load_default()

    print('Initializing IAQ calculator')
    iaq = IAQ()

    print('Initializing AQ Bar')
    aq_bar = AQ_Bar(draw)

    print('Starting main loop.')
    index = 0
    while True:
        print('Reset the image')
        image = Image.open(image_file)
        draw = ImageDraw.Draw(image)
        aq_bar = AQ_Bar(draw)


        inside.refresh_data()
        # the realtime data is updated only once per minute, so no reason to
        # refresh it any faster.
        if (index % round(60 / SLEEP)) == 0:
            outside.refresh_data()


        inside_name = inside.name[index % inside.size]
        inside_value = inside.value[index % inside.size]
        inside_unit = inside.unit[index % inside.size]
        # this string should be rendered
        inside_text = f"{inside_name}: {inside_value} {inside_unit}"
        outside_name = outside.name[index % outside.size]
        outside_value = outside.value[index % outside.size]
        outside_unit = outside.unit[index % outside.size]
        # this string should be rendered
        outside_text = f"{outside_name}: {outside_value} {outside_unit}"
        

        inside_air_quality = iaq.calculate_air_quality_score(inside.value[2], inside.value[1])


        draw.text((10, 60), inside_text, font=font, fill=(225, 225, 225))
        draw.text((10, 180), outside_text, font=font, fill=(225, 225, 225))
        aq_bar.render(inside_air_quality)


        # Must always be last
        disp.display(image)
        index = index + 1 if index < 1000 else 0
        time.sleep(SLEEP)


if __name__ == "__main__":
    main()