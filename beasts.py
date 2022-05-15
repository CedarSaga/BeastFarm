#beasts
from tempfile import TemporaryDirectory
from p5 import *
import numpy as np
import random

WIN_WID = 750
WIN_HEI = 500

#TODO: fix turning jitters

class Beast:
    def __init__(self):
        #generating three numbers to assign to color values
        self.color = Color(self.randNum(0,255),self.randNum(0,255),self.randNum(0,255))

        #generating random size variables 5 to 10
        self.radius = self.randNum(4,6)
        
        #position is a set of random numbers within the window range for x and y
        self.position = Vector(self.randNum(0, WIN_WID), self.randNum(0, WIN_HEI))

        #setting the velocity vector to two numbers
        self.velocity = Vector(self.randNum(-10,10), self.randNum(-10,10))
        Vector.normalize(self.velocity)
        self.velocity *= 5  

        #setting acceleration
        self.acc = Vector(0,0)

        
        self.perceptionRadius = self.randNum(75,90)

        self.maxSpeed = self.randNum(5,20)
        self.maxForce = 1


    def display(self):
        #using some p5 library graphics stuff to draw the bodies
        theta = self.velocity.angle + radians(90)
        stroke(0,0,0)
        fill(self.color)
        push_matrix()
        translate(self.position.x, self.position.y)
        rotate(theta)
        begin_shape()
        vertex(0, -self.radius * 2)
        vertex(-self.radius, self.radius * 2)
        vertex(self.radius, self.radius * 2)
        end_shape(CLOSE)
        pop_matrix()
        #circle(self.position, self.perceptionRadius) #perception circle for testing
        


    def move(self, flock):
        self.behave(flock)

        self.velocity += self.acc

        #limits acceleration to stop endless speeding up
        self.velocity.limit(self.maxSpeed)

        self.position += self.velocity
        self.acc *= 0

    def behave(self, flock):
        #Three behaviors are built similarly
        sep = self.separate(flock)
        ali = self.align(flock)
        coh = self.cohesion(flock)

        sep *= 1
        ali *= 1
        coh *= 1

        self.applyForce(sep)
        self.applyForce(ali)
        self.applyForce(coh)

    def separate(self, flock):
        #steering vector
        separate = Vector(0,0)
        total = 0

        for beast in flock:
            #Isnt itself and other beast is in the view range
            if (beast != self) & (dist(beast.position, self.position) < self.perceptionRadius):
                diff = Vector.__sub__(self.position, beast.position)
                diff /= pow(dist(beast.position, self.position),2)
                separate += diff
                total += 1
        if total > 0:
            separate /= total #take average of differences
            separate.magnitude = self.maxSpeed #go as fast as possible
            separate -= self.velocity
            separate.limit(self.maxForce)
        return separate
            

    def align(self, flock):
        alignment = Vector(0,0)
        total = 0

        for beast in flock:
            if (beast != self)&(dist(beast.position, self.position) < self.perceptionRadius):
                alignment += beast.velocity
                total += 1
        if total > 0:
            alignment /= total
            alignment -= self.velocity
            alignment.magnitude = self.maxSpeed
            alignment.limit(self.maxForce)
        return alignment

    def cohesion(self, flock):
        cohesion = Vector(0,0)
        total = 0
        for beast in flock:
            if (beast != self)&(dist(beast.position, self.position) < self.perceptionRadius):
                cohesion += beast.position
                total += 1
        if total > 0:
            cohesion /= total
            cohesion -= self.position
            cohesion.magnitude = self.maxSpeed
            cohesion.limit(self.maxForce)
        return cohesion

    def applyForce(self, force):
        #Mass would go here
        self.acc += force


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


    def randNum(self, low, high):
        return random_uniform(low=low, high=high)

"""
LEGACY

#from init
    #legacy for rectangles
        #self.width = np.random.randint(5,high=50)
        #self.height = np.random.randint(5,high=50)

#from display
    #legacy rectangles
        #rect_mode("CENTER")
        #rect(self.position.x, self.position.y, self.width, self.height)


        
"""