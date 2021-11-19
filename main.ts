input.onButtonPressed(Button.A, function () {
    pausa = 500
})
input.onButtonPressed(Button.B, function () {
    pausa = 1000
})
let pausa = 0
let pilota = game.createSprite(4, 2)
pausa = 50
basic.forever(function () {
    basic.pause(100)
    pilota.move(1)
    pilota.ifOnEdgeBounce()
})
