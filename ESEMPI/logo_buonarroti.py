from sense_hat import SenseHat

sense = SenseHat()

X = [30, 144, 255]  # Red
O = [0, 0, 0]  # White

logo_buonarroti = [
    O, O, X, O, X, O, O, O,
    O, O, O, O, O, X, O, O,
    O, O, O, O, O, O, X, O,
    O, O, O, X, O, X, O, O,
    O, O, X, O, X, O, O, O,
    O, O, X, O, O, O, X, O,
    O, O, X, O, O, X, O, O,
    O, O, X, O, X, O, O, O
]

sense.set_pixels(logo_buonarroti)
