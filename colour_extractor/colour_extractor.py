# pip install colorgram.py
import colorgram
# pip install Colr
from colr import color


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


rgb_colours = []
image_to_extract = input("Which Image you want to extract? ")
colours = colorgram.extract(image_to_extract, 50)
for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    rgb_colour = (r,g,b)
    rgb_colours.append(rgb_colour)


for colour in rgb_colours:
    print(color(f"RGB : {colour}, Hex code: #{rgb_to_hex(colour)}", fore=(0, 0, 0), back=colour))