def be_polite(fn):
	def wrapper():
		print("what a pleasure to meet you")
		fn()
		print("Have a great day")

	return wrapper

@be_polite
def greet():
	print("My name is aman")
@be_polite
def rage():
	print("I hate you")

# greet = be_polite(greet)
# rage = be_polite(rage)
greet()
rage()