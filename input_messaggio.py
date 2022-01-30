from sense_hat import SenseHat
sense = SenseHat()

# Non usare - non c'è input utente sulla ISS
messaggio = input("Inserisci il messaggio: ")
sense.show_message(messaggio)