"""
Title: Flappy
Creator: Me
Description: Clone of Flappy Bird
"""

# Setup
info.set_life(3)
info.set_score(0)
scene.set_background_color(6)
effects.bubbles.start_screen_effect()
game.splash("Flappy Fish","Press A to Start")
# Create Flappy
flappy = sprites.create(img("""
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
"""))
flappy.x = 40
flappy.ay = 45
def on_flap():
    flappy.vy = -45
controller.A.on_event(ControllerButtonEvent.PRESSED, on_flap)

def on_update():
    y = flappy.y
    if y > scene.screen_height():
        death()
    elif y < 0: 
        flappy.y = 0
game.on_update(on_update)

def death():
    info.change_life_by(-1)
    flappy.y = scene.screen_height()/2
    flappy.vy = 0
    game.splash("Press A to Restart")
# Cretae Columns
def create_column():
    colu
    game.on_update_interval(500, create_column)

# Check for Collidions
