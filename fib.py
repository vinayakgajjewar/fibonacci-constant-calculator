def calc_fib_constant(n, iter):
	# Here, n is the order of the Fibonacci sequence
	# n=2 corresponds to the classic Fibonacci sequence
	# iter is the number of iterations to go through
	# TODO: Make it work for n != 2

	# Starting numbers
	a = 0
	b = 1

	# The list holding the Fib numbers
	fib_nums = []

	# Populate the list with init values
	for i in range(n):
		fib_nums.append(a)
	fib_nums.append(b)

	# Now to calculate the rest of the sequence
	# TODO: Generalize this for n != 2
	for i in range(iter - 3):

		print("i: " + str(i))

		a = fib_nums[len(fib_nums) - 1]
		print("a: " + str(a))

		b = fib_nums[len(fib_nums) - 2]
		print("b: " + str(b))

		next_num = a + b
		print("next_num: " + str(next_num))
		fib_nums.append(next_num)

	print(fib_nums)

# Regular old Fibonacci sequence
calc_fib_constant(2, 10)