def reverse_array1(arr):
	result = arr[::-1]
	return result

print(reverse_array1([1,2,3,4,5]))


def reverse_array2(arr):
	start = 0
	end = len(arr)-1
	while start<=end:
		arr[start], arr[end] = arr[end], arr[start]
		# arr[start] = arr[end]
		# arr[end] = arr[start]
		print(arr)
		start += 1
		end -= 1
	return arr

print(reverse_array2([5,4,3,2,1]))



