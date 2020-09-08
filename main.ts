/** 
Title: Flappy
Creator: Me
Description: Clone of Flappy Bird

 */
//  Setup
info.setLife(3)
info.setScore(0)
scene.setBackgroundColor(6)
effects.bubbles.startScreenEffect()
game.splash("Flappy Fish", "Press A to Start")
//  Create Flappy
let flappy = sprites.create(img`
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . 1 . . .
    . . f f f f f f f f f f 1 1 . .
    . . f f f f f f f f f f 1 1 . .
    . . f f f f f f f f f f 1 1 . .
    . . f f f f f f f f f f 1 . . .
    . . f f f . . . . f f 1 1 . . .
    . . . . . . . . . . . 1 . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
`)
flappy.x = 40
flappy.ay = 45
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_flap() {
    flappy.vy = -45
})
game.onUpdate(function on_update() {
    let y = flappy.y
    if (y > scene.screenHeight()) {
        death()
    } else if (y < 0) {
        flappy.y = 0
    }
    
})
function death() {
    info.changeLifeBy(-1)
    flappy.y = scene.screenHeight() / 2
    flappy.vy = 0
    game.splash("Press A to Restart")
}

//  Cretae Columns
