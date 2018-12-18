class rectangle(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
	def Area(self):	
		return self.width * self.height
	def Perimeter(self):
		return (self.width + self.height) *2

#rectangle1= rectangle(15,20)
#print (rectangle1.Area())
# #print(rectangle1.Perimeter())
# class Person(object):
# 	def __init__(self, name, age, city, gender):
# 		self.name= name
# 		self.age = age
# 		self.city = city
# 		self.gender = gender
# 	def eat(self,favorite):
# 		print(self.name, "is eating" + favorite)
# 	def play(self,fav_sport):
# 		print(self.name, "is playing" + fav_sport)
# person1 = person(Amir,15,Nazareth, M)

class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)
flower_song = Song(["roses are red,", "Violets are blue,", " I wrote this poem for you."])
flower_song.sing_me_a_song()