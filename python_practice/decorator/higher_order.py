def sum(n, func):
	total = 0
	for num in range(1, n+1):
		total+=func(num)
	return total

def square(num):
	return num*num

def cube(num):
	return num*num*num

print(sum(3, square))
print(sum(2, cube))