class Pair:
	def __init__(self):
		self.min = 0
		self.max = 0

def get_min_max(arr):
	min_max = Pair()

	# If there is only one element then return it as min and max both
	arr_length = len(arr)
	if arr_length==1:
		min_max.min, min_max.max = arr[0], arr[0]
		return min_max

	if arr[0]>arr[1]:
 		min_max.min, min_max.max = arr[1], arr[0]
	else:
		min_max.min, min_max.max = arr[0], arr[0]

	for i in range(2, arr_length):
		if arr[i]>min_max.max:
			min_max.max = arr[i]

		elif arr[i]<min_max.min:
			min_max.min = arr[i]

	return min_max



result = get_min_max([0, 4,2,7,3, 10])
print(result.min, result.max)

