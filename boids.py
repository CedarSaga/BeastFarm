#boids
from p5 import *
import numpy as np

WIN_WID = 1000
WIN_HEI = 1000

class Beast:
    def __init__(self):
        x=0
        y=0

        self.maxSpeed = 5
        self.maxForce = .3

        self.position = Vector((np.random.randint(0, high=WIN_WID)), (np.random.randint(0, high=WIN_HEI)))
        vec = (np.random.rand(2) - .5)*10
        self.velocity = Vector(*vec)

        vec = (np.random.rand(2) - .5)/2
        self.acc = Vector(*vec)
        
        col1 = np.random.randint(0, high=255)
        col2 = np.random.randint(0, high=255)
        col3 = np.random.randint(0, high=255)
        
        self.color = Color(col1, col2, col3)

        self.width = np.random.randint(5,high=10)
        self.height = np.random.randint(5,high=10)
        self.size = self.width*self.height

    def display(self):
        stroke(0)
        fill(self.color)
        rect_mode("CENTER")
        rect((self.position.x, self.position.y), self.width, self.height)

    def move(self):
        self.position += self.velocity
        self.velocity += self.acc
        if np.linalg.norm(self.velocity) > 3:
            self.velocity = self.velocity / np.linalg.norm(self.velocity) * 3

        self.acceleration = Vector(*np.zeros(2))

    def edges(self):
        if self.position.x > WIN_WID:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = WIN_WID
        
        if self.position.y > WIN_HEI:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = WIN_HEI


