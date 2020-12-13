from PIL import ImageDraw

class AQ_Bar():
    def __init__(self, draw: ImageDraw.Draw) -> None:
        # "draw" might need to be returned once drawing is done
        self.draw = draw

    def __get_color(self, value: int):
        if value > 66:
            # green
            return (0, 255, 0)
        elif value > 33:
            # yellow
            return (255, 255, 0)
        else:
            # red
            return (255, 0, 0)

    def render(self, value: int):
        # total 240 px
        # top padding 10 px, 230 left
        # bot padding 10 px, 220 left
        # left padding is 5 pixels
        # right padding is 5 pixels
        # a continuous bar 220 pix long
        # so the size of the rectangle should be proportional to "value"

        # let's imagine the value is between 0 and 100
        # the bar section is between pixels 187 and 240

        # top left is (0,0)
        x0 = 192                    # top left
        # y0 = round(230*value/100)   # top left
        y0 = 230                      # top left
        x1 = 235                    # bottom right
        y1 = round(240 - 220*value/100 - 10)    # bottom right
        rectangle_size = (x0, y0, x1, y1)

        color = self.__get_color(value)
        self.draw.rectangle(rectangle_size, fill=color, outline=color) 

        # maybe needed ?
        # return self.draw
