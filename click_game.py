ghost=Actor('ghost.png')
ghost.pos = 100,500


WIDTH= 700
HEIGHT = 1000

def draw ():
    screen.fill((178,172,136))
    ghost.draw()

def update():
    ghost.left=ghost.left + 2
    if ghost.left > 400:
        ghost.right = 0
