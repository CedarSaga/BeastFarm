from boids import *


flock = [Beast() for _ in range(20)]

def setup():
    global flock
    size(WIN_WID, WIN_HEI)

def draw():
    global flock
    background(30, 30, 47)

    for beast in flock:
        beast.move()
        beast.display()
        beast.edges()

if __name__ == '__main__':
    run()