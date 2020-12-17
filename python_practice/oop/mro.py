class A:
	def do_something(self):
		print("Method defined in: A")

class B(A):
	def do_something(self):
		print("Method defined in: B")
		# super().do_something()
class C(A):
	def do_something(self):
		print("Method defined in: C")

class D(B,C):
	def do_something(self):
		print("Method defined in: D")
		super().do_something()

# print(D.__mro__)
# print(D.mro())
# print(help(D))

thing = D()
thing.do_something()