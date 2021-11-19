def on_button_pressed_a():
    global pausa
    pausa = 500
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global pausa
    pausa = 1000
input.on_button_pressed(Button.B, on_button_pressed_b)

pausa = 0
pilota = game.create_sprite(4, 2)
pausa = 50

def on_forever():
    basic.pause(100)
    pilota.move(1)
    pilota.if_on_edge_bounce()
basic.forever(on_forever)
