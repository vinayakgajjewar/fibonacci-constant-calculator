# For printing to n decimal places
import decimal
decimal.getcontext().prec = 150

def calc_fib_constant(n, count):
	# Here, n is the order of the Fibonacci sequence
	# n=2 corresponds to the classic Fibonacci sequence
	# count is the number of Fibonacci numbers to generate
	# TODO: Make it work for n != 2

	temp_list = [0, 0]

	# The list holding the Fib numbers
	fib_nums = []

	# Populate the list with init values
	for i in range(n - 1):
		fib_nums.append(0)
	fib_nums.append(1)

	# Now to calculate the rest of the sequence
	# TODO: Generalize this for n != 2
	for i in range(count - 2):

		# print("i: " + str(i))

		temp_list[0] = fib_nums[len(fib_nums) - 1]

		temp_list[1] = fib_nums[len(fib_nums) - 2]

		next_num = temp_list[0] + temp_list[1]
		# print("next_num: " + str(next_num))
		fib_nums.append(next_num)

	print(fib_nums)

	r = decimal.Decimal(fib_nums[len(fib_nums) - 1]) / decimal.Decimal(fib_nums[len(fib_nums) - 2])
	print(r)

# Regular old Fibonacci sequence
calc_fib_constant(2, 10)
# calc_fib_constant(2, 100)
# calc_fib_constant(2, 1000)
# calc_fib_constant(2, 10000)
# calc_fib_constant(2, 100000)
