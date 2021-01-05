def reverse_digit(nums):
	rev_num = 0
	while nums>0:
		temp = nums%10
		rev_num = rev_num*10+temp
		nums = nums//10
	
	return rev_num

print(reverse_digit(12345))

# using recursion
base_pos = 1
rev_num = 0
def reverse_digit_recursion(nums):
	global base_pos
	global rev_num
	if nums>0:
		reverse_digit_recursion(nums//10)
		rev_num += nums%10*base_pos
		base_pos *= 10
		print("dffd")

	return rev_num

print(reverse_digit_recursion(1002))


