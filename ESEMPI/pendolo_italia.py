from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

sfondo = (255,255,255)
filo  = (255,0,0)
palla = (0,115,5)

W = palla
M = filo
O = sfondo


def a():
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    M, O, O, O, O, O, O, O,
    M, O, O, O, O, O, O, O,
    O, M, O, O, O, O, O, O,
    O, O, M, M, O, O, O, O,
    O, O, O, O, M, M, O, O,
    
    ]
    return logo
    
def b():
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    M, O, O, O, O, O, O, O,
    M, O, O, O, O, O, O, O,
    O, M, M, O, O, O, O, O,
    O, O, O, M, M, O, O, O,
    O, O, O, O, O, M, O, O,
    
    ]
    return logo
    
def c():
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    M, O, O, O, O, O, O, O,
    M, M, O, O, O, O, O, O,
    O, O, M, M, O, O, O, O,
    O, O, O, O, M, M, O, O,
    O, O, O, O, O, O, W, W,
    
    ]
    return logo
    
def d():
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    M, O, O, O, O, O, O, O,
    M, M, M, M, O, O, O, O,
    O, O, O, O, M, M, O, O,
    O, O, O, O, O, O, W, W,
    O, O, O, O, O, O, W, W,
    
    ]
    return logo

def e():
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    M, O, O, O, O, O, O, O,
    M, M, M, M, M, O, O, O,
    O, O, O, O, O, M, W, W,
    O, O, O, O, O, O, W, W,
    O, O, O, O, O, O, O, O,
    
    ]
    return logo

def f():
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    M, O, O, O, O, O, O, O,
    M, M, M, M, M, M, W, W,
    O, O, O, O, O, O, W, W,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    
    ]
    return logo
    
def g():
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    M, M, M, M, M, M, W, W,
    M, M, M, M, M, M, W, W,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    
    ]
    return logo

def h():
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, W, W,
    M, M, M, M, M, M, W, W,
    M, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    
    ]
    return logo

def i():
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, W, W,
    O, O, O, O, O, M, W, W,
    M, M, M, M, M, O, O, O,
    M, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    
    ]
    return logo
    
def j():
    logo = [
    O, O, O, O, O, O, W, W,
    O, O, O, O, O, O, W, W,
    O, O, O, O, M, M, O, O,
    M, M, M, M, O, O, O, O,
    M, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    
    ]
    return logo

def k():
    logo = [
    O, O, O, O, O, O, W, W,
    O, O, O, O, M, M, O, O,
    O, O, M, M, O, O, O, O,
    M, M, O, O, O, O, O, O,
    M, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    
    ]
    return logo

def l():
    logo = [
    O, O, O, O, O, M, O, O,
    O, O, O, M, M, O, O, O,
    O, M, M, O, O, O, O, O,
    M, O, O, O, O, O, O, O,
    M, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    
    ]
    return logo
    
def m():
    logo = [
    O, O, O, O, M, M, O, O,
    O, O, M, M, O, O, O, O,
    O, M, O, O, O, O, O, O,
    M, O, O, O, O, O, O, O,
    M, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    
    ]
    return logo

images = [a,b,c,d,e,f,g,h,i,j,k,l,m,l,k,j,i,h,g,f,e,d,c,b,a]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.1)
    count += 1
