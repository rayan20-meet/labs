import turtle
from turtle import Turtle
import random

# class Square(Turtle):
# 	def __init__(self, size):
# 		Turtle.__init__(self)
# 		self.shapesize(size)
# 		self.shape("square")
# 	def Random_color(self):
# 		r= random.random()
# 		g = random.random()
# 		b = random.random()
# 		self.color(r,g,b)


# s = Square(25)
# for i in range(5):
# 	s.Random_color()
class Hexagon(Turtle):
	def __init__(self, size):
		self.size=size
		Turtle.__init__(self)
		turtle.home()
		turtle.begin_poly()
		turtle.penup()
		turtle.left(90)
		turtle.fd(self.size)
		turtle.right(60)
		turtle.pendown()
		turtle.fd(self.size)
		turtle.right(60)
		turtle.fd(self.size)
		turtle.right(60)
		turtle.fd(self.size)
		turtle.right(60)
		turtle.fd(self.size)
		turtle.right(60)
		turtle.fd(self.size)
		turtle.right(60)
		turtle.fd(self.size)
		turtle.right(60)

		turtle.end_poly()
		p =turtle.get_poly()
		turtle.register_shape("Hexagon", p)


hex = Hexagon(100)
turtle.mainloop()