print("FACTORIAL PROGRAMMING")

num = eval(input("Enter any number to identify the factorial: "))
factorial = num

for x in range(num-1, 0, -1):
	result = factorial *x
	print(factorial, "multiplied by ", x, " is", result)
	factorial = result
print("Therefore the factorial of the", num, "is", factorial)
