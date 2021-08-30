from escpos.printer import Usb
from escpos import *

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

width = 500
height = 250

image = Image.new('1', (width, height), 255)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('Corporate-Logo-Rounded.ttf', 50, encoding='unic')
draw.text((0, 0), "日本語" + " ", font=font, fill=0)
font = ImageFont.truetype('Corporate-Logo-Rounded.ttf', 28, encoding='unic')
draw.text((0, 82), "abcdefghijklmnopqrstuvwxyz", font=font, fill=0)
draw.text((0, 112), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", font=font, fill=0)
draw.text((0, 142), "1234567890" + " ", font=font, fill=0)
draw.text((0, 172), "!\"#$%&'()=~|+*<>?_{}" + " ", font=font, fill=0)

p = Usb(0x0416, 0x5011, 0, 0x81, 0x03)
p.text("Hello World\n")
p.image(image)
p.cut()