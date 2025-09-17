#Multiplication Table Maker
print("MULTIPLICATION TABLE MAKER")

#ask the user for a number 
num = eval(input("Enter number: "))
#Loop from 1-10 
for i in range (1, 11):
    result = num * i 
    print(num, "x", i, " = ", result)
