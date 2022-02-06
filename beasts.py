#beasts
from p5 import *
import numpy as np

WIN_WID = 1000
WIN_HEI = 1000

class Beast:
    def __init__(self):
        #position is a set of random numbers within the window range for x and y
        self.position = Vector((np.random.randint(0, high=WIN_WID)), (np.random.randint(0, high=WIN_HEI)))

        #setting the velocity vector to two numbers, I believe something ~.01--
        vec = (np.random.rand(2) - .5)*10
        self.velocity = Vector(*vec)

        #setting acceleration to two numbers, I believe something ~.0005--
        vec = (np.random.rand(2) - .5)/2
        self.acc = Vector(*vec)
        
        #generating three numbers to assign to color values
        col1 = np.random.randint(0, high=255)
        col2 = np.random.randint(0, high=255)
        col3 = np.random.randint(0, high=255)
        self.color = Color(col1, col2, col3)

        #generating random size variables 5 to 10, setting up a size combination for bouncing later maybe?
        self.width = np.random.randint(5,high=10)
        self.height = np.random.randint(5,high=10)
        self.size = self.width*self.height

    def display(self):
        #using some p5 library graphics stuff to draw the bodies
        stroke(0)
        fill(self.color)
        rect_mode("CENTER")
        rect((self.position.x, self.position.y), self.width, self.height)

    def move(self):
        #moves position, adds acceleration to vary speed
        self.position += self.velocity
        self.velocity += self.acc

        #limits acceleration to stop endless speeding up
        if np.linalg.norm(self.velocity) > 3:
            self.velocity = self.velocity / np.linalg.norm(self.velocity) * 3
        #resets acceleration
        self.acceleration = Vector(*np.zeros(2))

    def edges(self):
        #wraps around
        if self.position.x > WIN_WID:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = WIN_WID
        
        if self.position.y > WIN_HEI:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = WIN_HEI


