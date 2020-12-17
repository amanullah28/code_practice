class Person:
	def __init__(self):
		self.name = "Tony"
		self._secret = "hi"
		self.__msg = "I like turtle"
		self.__lol = "HAHAHAHAH"

	def __repr__(self):
		# return f"Your name is {self.name}"
		print("in repr")

p = Person()
print(p)
# print(p.name, p._secret)
print(p._Person__msg)
# print(dir(p))