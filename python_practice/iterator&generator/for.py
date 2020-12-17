def my_for(iterable, func):
	iterator = iter(iterable)
	while True:
		try:
			thing = next(iterator)
		except StopIteration:
			break
		else:
			func(thing)


def square(num):
	int_num = int(num)
	print(int_num*int_num)

my_for("lol", print)
my_for([1,2,3], square)
