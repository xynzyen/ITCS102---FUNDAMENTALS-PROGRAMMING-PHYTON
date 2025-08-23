#name
#specify if student or not
#fare or bayad
#discount

passenger = input("Input your name: ")
passenger1 = input("Are you a student (Yes / No): ")
fare = eval(input("Fare: "))

if passenger == "yes" :
	discount = fare * .15
	newfare = fare - .15
	print("Congrats discount has been approved your discounted fare is",newfare,  "Enjoy your ride with us")
else:
	print("Sorry your request to have a discount has not been approved")