print("SUMMATION OF ODD NUMBERS")

total = 0

for i in range(10):
	num = eval(input("Enter 10 numbers to sum all the odd numbers: "))
	if num % 2 != 0:
		total += num

print("The sum of all the ODD numbers is", total)