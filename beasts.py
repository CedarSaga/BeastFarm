#beasts
from tempfile import TemporaryDirectory
from p5 import *
import numpy as np

WIN_WID = 500
WIN_HEI = 500

class Beast:
    def __init__(self):

        #generating random size variables 5 to 10, setting up a size combination for bouncing later maybe?
        self.radius = random_uniform(low=5,high=15)
        #self.width = np.random.randint(5,high=50)
        #self.height = np.random.randint(5,high=50)
        
        self.perception = self.radius + 50

        #position is a set of random numbers within the window range for x and y
        self.position = Vector((random_uniform(low=0, high=WIN_WID)), (random_uniform(low=0, high=WIN_WID)))

        self.speedMult = self.radius / 2

        #setting the velocity vector to two numbers
        vec1 = random_uniform(low=1,high=15)
        vec2 = random_uniform(low=1,high=15)
        vec = (vec1, vec2) 
        self.velocity = Vector(*vec)
        Vector.normalize(self.velocity)
        self.velocity /= self.speedMult

        #setting acceleration to two numbers
        vec1 = random_uniform(low=(-.001), high=.001)
        vec2 = random_uniform(low=(-.001), high=.001)
        vec = (vec1, vec2) 
        self.acc = Vector(*vec)
        Vector.normalize(self.acc)
        self.acc *= .5
        
        #generating three numbers to assign to color values
        col1 = random_uniform(low=0, high=255)
        col2 = random_uniform(low=0, high=255)
        col3 = random_uniform(low=0, high=255)
        self.color = Color(col1, col2, col3)


    def display(self):
        #using some p5 library graphics stuff to draw the bodies
        stroke(0,0,0)
        fill(self.color)
        circle(self.position.x, self.position.y, self.radius)
        #rect_mode("CENTER")
        #rect(self.position.x, self.position.y, self.width, self.height)

    def move(self):
        #moves position, adds accelercation to vary speed
        self.velocity += self.acc
        

        #limits acceleration to stop endless speeding up
        self.velocity.limit(1)

        self.position += self.velocity

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

    #This does not work
    def bounce(self, flock):
        for beast in flock:
            distance = Vector.distance(self.position, beast.position)
            radSum = self.radius + beast.radius
            #if distance < radSum:
            radSum = 0
            distance = 0
