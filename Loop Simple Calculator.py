#loopable calculator

#Calculator Function
def simpcalc() :
	num1 = float(input("Enter first number: "))
	print("Operator examples : (+, - , *, /)")
	op = input("Enter an operator: ")
	num2 = float(input("Enter your second number: "))
	
#Defining operators
	addition = num1 + num2
	subtraction = num1 - num2
	division = num1 / num2
	multiplication = num1 * num2

	if op == "+" :
		print(addition)
	elif op == "-" :
		print(subtraction) 
	elif op == "/" :
		print(division)
	elif op == "*" :
		print (multiplication)
	else:
		print("Invalid operator")
	loopcalc()

#LOOPING FUNCTION
def loopcalc() :
	repeat = input('''Would you like to keep going?
	Please answer Y/N.''')
	
	if repeat == "Y" :
		simpcalc()
		
	elif repeat == "N":
		print("Understood, have a great day!")
		
	else:
		print("Invalid answer, please try again")
		loopcalc()
		
		
#calling the function
simpcalc()
