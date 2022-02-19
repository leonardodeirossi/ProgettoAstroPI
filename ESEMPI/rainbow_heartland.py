from sense_hat import SenseHat
import time

# Create a sense object
sense = SenseHat()
    
# Reduce the brightness of the LED display
sense.low_light = True

# Create variables to hold each RGB color we want to use
r = (255, 0, 0)     # red 
p = (204, 0, 204)   # pink
o = (255, 128, 0)   # orange
y = (255, 255, 0)   # yellow
g = (0, 255, 0)     # green
a = (0, 255, 255)   # aqua
b = (0, 0, 255)     # blue
pr = (128, 0, 255)  # purple
e = (0, 0, 0)       # blank

# Create a list to hold the color of each pixel in our heart images
# Each image contains 8 rows of 8 pixels each
red_heart = [
     r, r, r, r, r, r, r, r,
     r, r, r, r, r, r, r, r,
     r, r, r, r, r, r, r, r,
     r, r, r, r, r, r, r, r,
     r, r, r, r, r, r, r, r,
     r, r, r, r, r, r, r, r,
     r, r, r, r, r, r, r, r,
     r, r, r, r, r, r, r, r
     ]

pink_heart = [
     p, p, p, p, p, p, p, p,
     p, p, p, p, p, p, p, p,
     p, p, p, p, p, p, p, p,
     p, p, p, p, p, p, p, p,
     p, p, p, p, p, p, p, p,
     p, p, p, p, p, p, p, p,
     p, p, p, p, p, p, p, p,
     p, p, p, p, p, p, p, p
     ]

orange_heart = [
     o, o, o, o, o, o, o, o,
     o, o, o, o, o, o, o, o,
     o, o, o, o, o, o, o, o,
     o, o, o, o, o, o, o, o,
     o, o, o, o, o, o, o, o,
     o, o, o, o, o, o, o, o,
     o, o, o, o, o, o, o, o,
     o, o, o, o, o, o, o, o
     ]

yellow_heart = [
     y, y, y, y, y, y, y, y,
     y, y, y, y, y, y, y, y,
     y, y, y, y, y, y, y, y,
     y, y, y, y, y, y, y, y,
     y, y, y, y, y, y, y, y,
     y, y, y, y, y, y, y, y,
     y, y, y, y, y, y, y, y,
     y, y, y, y, y, y, y, y
     ]

green_heart = [
     g, g, g, g, g, g, g, g,
     g, g, g, g, g, g, g, g,
     g, g, g, g, g, g, g, g,
     g, g, g, g, g, g, g, g,
     g, g, g, g, g, g, g, g,
     g, g, g, g, g, g, g, g,
     g, g, g, g, g, g, g, g,
     g, g, g, g, g, g, g, g
     ]

aqua_heart = [
     a, a, a, a, a, a, a, a,
     a, a, a, a, a, a, a, a,
     a, a, a, a, a, a, a, a,
     a, a, a, a, a, a, a, a,
     a, a, a, a, a, a, a, a,
     a, a, a, a, a, a, a, a,
     a, a, a, a, a, a, a, a,
     a, a, a, a, a, a, a, a
     ]

blue_heart = [
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, b, b
     ]

purple_heart = [
     pr, pr, pr, pr, pr, pr, pr, pr,
     pr, pr, pr, pr, pr, pr, pr, pr,
     pr, pr, pr, pr, pr, pr, pr, pr,
     pr, pr, pr, pr, pr, pr, pr, pr,
     pr, pr, pr, pr, pr, pr, pr, pr,
     pr, pr, pr, pr, pr, pr, pr, pr,
     pr, pr, pr, pr, pr, pr, pr, pr,
     pr, pr, pr, pr, pr, pr, pr, pr
     ]

heart_colors = [red_heart, pink_heart, orange_heart, yellow_heart,
                green_heart, aqua_heart, blue_heart, purple_heart]

def rainbow_hearts():

    for color in heart_colors:
        sense.set_pixels(color)
        time.sleep(1)

    # Clear the LED display
    sense.clear()

while True:
    rainbow_hearts()