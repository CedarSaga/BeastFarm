from beasts import *

FLK_SIZ = 10
flock = [Beast() for _ in range(FLK_SIZ)]

def setup():
    global flock, beast
    size(WIN_WID, WIN_HEI)
    
def draw():
    global flock, beast
    background(70, 0, 150)
    
    
    for beast in flock:
        beast.display()
        beast.move(flock)
        edges(beast)
    

if __name__ == '__main__':
    run()
