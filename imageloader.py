#!/usr/bin/python

import sys
import os
import logging
import time
import traceback

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "lib"))

from waveshare_epd import epd2in13bc
from PIL import Image

logging.basicConfig(level=logging.DEBUG)
logging.info("Image Loader")

blackImage = None;
colorImage = None;

if len(sys.argv) < 2: 
    logging.info("No images provided.")
    exit()

images = sys.argv[1:len(sys.argv)]

logging.info("Loading images:")
print(images)
logging.info(len(images))

try:
    epd = epd2in13bc.EPD()
    epd.init()
    epd.Clear()
    
    time.sleep(1)
   
    blackImage = Image.open(os.path.realpath(images[0]), "r")

    if len(images) > 1:
        colorImage = Image.open(os.path.realpath(images[1]), "r")
    else:
        colorImage = Image.new("1", (epd.width, epd.height), 255)
    
    # The function checks already if the image is none.
    epd.display(epd.getbuffer(blackImage), epd.getbuffer(colorImage))
    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("CTRL+C")
    epd2in13bc.epdconfig.module_exit()
    exit()
