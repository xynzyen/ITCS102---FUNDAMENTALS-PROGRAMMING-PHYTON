end = 0

for me in range(1,11):
    meow = eval(input("enter number: "))
    if meow % 2 == 1:
        end += meow
print(f"The summation of all number is {end}")
