# def fib_list(max):
# 	nums = []
# 	a, b = 0, 1
# 	while len(nums)<max:
# 		nums.append(b)
# 		a, b = b, a+b
# 	return nums

# fib = fib_list(100000)
# print(fib)


def fib_gen(max):
	x, y = 0, 1
	count = 0
	while count<max:
		x, y = y, x+y
		yield x
		count+=1

for n in fib_gen(10000000):
	print(n)
