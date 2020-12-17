# Inheritance Example Using Super()
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")



blue = Cat("Blue","Scottish Fold", "String")
blue.play()


# OUR "MODEL" FOR ANIMAL AND CAT
# Animal
# 	species
# 	name

# Cat
# 	species
# 	name
# 	breed
# 	favorite_toy






# class Animal:
# 	def __init__(self, name, species):
# 		self.name = name
# 		self.species = species

# 	def __repr__(self):
# 		return f"{self.name} is a {self.species}"

# 	def make_sound(self, sound):
# 		print(f"This animal says {sound}")

# class Cat(Animal):
# 	def __init__(self, name, breed, toy):
# 		super.__init__(self, name, species = "Cat")
# 		self.breed = breed
# 		self.toy = toy



# blue = Cat("Blue", "Scottish Fold", "String")
# print(blue)
# # a = Animal()
# # print(a.make_sound("MEow!!"))
# # blue = Cat()
# # blue.make_sound("MEOW!!	")
# # print(blue.cool)
# # print(Animal.cool)
# # print(Cat.cool)

# # print(isinstance(blue, Animal))
# # print(isinstance(blue, Cat))
# # print(isinstance(blue, object))
