from beasts import *

FLK_SIZ = 25
flock = [Beast() for _ in range(FLK_SIZ)]

def setup():
    global flock, beast
    size(WIN_WID, WIN_HEI)
    
def draw():
    global flock, beast
    background(30, 30, 47)
    
    
    for beast in flock:
        beast.display()
        beast.move(flock)
        beast.edges()
    

if __name__ == '__main__':
    run()
