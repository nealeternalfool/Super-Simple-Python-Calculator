#loopable calculator

#Calculator Function
def simpcalc() :
	num1 = float(input("Enter first number: "))
	
	print("Operator examples : (+, - , *, /)")
	op = input("Enter an operator: ")
	
	num2 = float(input("Enter your second number: "))

	if op == "+" :
		result = num1 + num2
		
	elif op == "-" :
		result = num1 - num2
		
	elif op == "/" :
		if num2 != 0 :
			result = num1 / num2
		else:
			result = "Can't divide by 0"
	
	elif op == "*" :
		result = num1 * num2
		
	else:
		result = "Invalid operator"

	print(result)

	loopcalc()

#LOOPING FUNCTION
def loopcalc() :
	repeat = input('''Would you like to keep going?
	Please answer Y/N.''')
	
	if repeat == "Y" :
		simpcalc()

	elif repeat == "N":
		print("Understood, have a great day!")
		return
		
	else:
		print("Invalid answer, please try again")
		loopcalc()

#calling the function
simpcalc()