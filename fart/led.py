import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 2, auto_write=False)
pixels[0] = (255, 0, 0)
pixels[1] = (255, 255, 255)
pixels.show()
time.sleep(2)
pixels[0] = (0, 0, 0)
pixels[1] = (0, 0, 0)
pixels.show()