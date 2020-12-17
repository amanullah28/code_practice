def count_up_to(max):
	count = 1
	while count<=max:
		yield count
		count += 1

gen = count_up_to(10)
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# print(list(gen))
# print(help(gen))

for count in gen:
	print(count)
