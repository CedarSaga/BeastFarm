from beasts import *


flock = [Beast() for _ in range(20)]

def setup():
    global flock, beast
    size(WIN_WID, WIN_HEI)

def draw():
    global flock, beast
    background(30, 30, 47)

    for beast in flock:
        beast.move()
        beast.display()
        beast.edges()
        #beast.bounce(flock) Non-Functional

if __name__ == '__main__':
    run()