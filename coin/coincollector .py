from random import randint
WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

bunny = Actor("bunny")
bunny.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill((173, 216, 230 ))
    bunny.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black" , topleft=(10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)
def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def on_mouse_down(pos):
    if coin.collidepoint(pos):
        sounds.eep.play()

def time_up():
    global game_over
    game_over = True

def update():
    global score

    if keyboard. left:
        bunny.x = bunny.x - 2
    elif keyboard.right:
        bunny.x = bunny.x + 2
    elif keyboard.up:
        bunny.y = bunny.y - 2
    elif keyboard.down:
        bunny.y = bunny.y + 2

    coin_collected = bunny.colliderect(coin)

    if coin_collected:
        score = score + 10
        place_coin()

clock.schedule(time_up, 7.0)
place_coin()
