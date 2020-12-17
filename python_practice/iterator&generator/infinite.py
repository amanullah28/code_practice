
# def current_beat():
# 	max = 100
# 	nums = (1,2,3,4)
# 	i = 0
# 	result = []
# 	while len(result)<max:
# 		if i>=len(nums): i = 0
# 		result.append(nums[i])
# 		i += 1
# 	return result

# beat = current_beat()
# print(beat)


# By using generator

def current_beat():
	nums = (1,2,3,4)
	i = 0
	while True:
		if(i>=len(nums)): i = 0
		yield nums[i]
		i+=1


beat = current_beat()
# print(next(beat))
# print(next(beat))
# for b in beat:
# 	print(b)