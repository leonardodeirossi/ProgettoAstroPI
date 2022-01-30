from sense_hat import SenseHat

sense = SenseHat()

X = [0, 0, 255]  # Blue
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
