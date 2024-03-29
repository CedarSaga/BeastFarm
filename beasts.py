#beasts
from turtle import speed
from p5 import *

WIN_WID = 750
WIN_HEI = 500

#TODO: add main brain to determine independent direction

class Beast:
    def __init__(self):
        #generating three numbers to assign to color values
        self.color = Color(randNum(0,255), randNum(0,255),randNum(0,255))

        #generate political sway
        self.sway = self.color.r + self.color.b + self.color.g

        #generating random size variables 5 to 10
        self.mass = randNum(3,7)
        
        #position is a set of random numbers within the window range for x and y
        self.position = Vector(randNum(0, WIN_WID), randNum(0, WIN_HEI))

        #setting the velocity vector to two numbers
        self.velocity = Vector(randNum(-100,100), randNum(-100,100))
        
        self.speed = sqrt(self.velocity.x*self.velocity.x + self.velocity.y*self.velocity.y)

        #setting acceleration
        self.acc = (self.velocity / 10) #Vector(0,0)

        
        self.perceptionRadius = self.mass * 100 #randNum(75,90)
        self.personalSpace = self.mass * 10

  
        self.maxSpeed = 100
        self.minSpeed = 20
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
        vertex(0, -self.mass * 2)
        vertex(-self.mass, self.mass * 2)
        vertex(self.mass, self.mass * 2)
        end_shape(CLOSE)
        pop_matrix()

        #perception circle for testing
        #circle(self.position, self.perceptionRadius) 
    

    def move(self, flock):
        self.behave(flock)
        self.velocity += self.acc
    
        self.velocity.limit(self.maxSpeed)
        
        if (self.speed < self.minSpeed):
            self.velocity.x /= self.speed
            self.velocity.x *= self.minSpeed
            self.velocity.y /= self.speed
            self.velocity.y *= self.minSpeed

        self.position += self.velocity
        self.acc *= 0

    def behave(self, flock):
        #Three behaviors are built similarly
        sep = self.separate(flock)
        ali = self.align(flock)
        coh = self.cohesion(flock)

        sep *= 1
        ali *= .5
        coh *= .75 

        self.applyForce(sep)
        self.applyForce(ali)
        self.applyForce(coh)

    def separate(self, flock):
        #steering vector
        separate = Vector(0,0)
        total = 0

        for beast in flock:
            d = dist(beast.position, self.position) 
            if (beast != self) & (d < self.personalSpace): #Isnt itself and other beast is in the its space
                diff = self.position - beast.position
                diff /= pow(d,2)
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
            d = dist(beast.position, self.position)
            if (beast != self) & (d < self.perceptionRadius):
                alignment += beast.velocity
                total += 1
        if total > 0:
            alignment /= total
            alignment -= self.velocity
            alignment.magnitude = (self.maxSpeed / 2)
            alignment.limit(self.maxForce)
        return alignment

    def cohesion(self, flock):
        cohesion = Vector(0,0)
        total = 0

        for beast in flock:
            d = dist(beast.position, self.position)
            if (beast != self) & (d < self.perceptionRadius):
                cohesion += beast.position
                total += 1
        if total > 0:
            cohesion /= total
            cohesion -= self.position
            cohesion.magnitude = self.maxSpeed
            cohesion.limit(self.maxForce)
        return cohesion

    #def eat(self, food):

    def applyForce(self, force):
        #Mass goes here
        self.acc += (force / self.mass)


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

def randNum(low, high):
    return random_uniform(low=low, high=high)
