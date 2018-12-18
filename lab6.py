from turtle import *
import random
import math
class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
ball1 = Ball(10, "black", 89)
ball2 = Ball(15, "blue", 95)
ball_list=[baal1,ball2]
def check_collision(ball1,ball2):
	r1 = ball1.radius
	r2 = ball2.radius
	x1 = ball1.position()[0]
	x2 = ball2.position()[0]
	y1 = ball1.position()[1]
	y2 = ball2.position()[1]
	d = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if r1+r2>= d:
		print("collision")
	else:
		print ("no collision")
check_collision(ball1,ball2)
mainloop()