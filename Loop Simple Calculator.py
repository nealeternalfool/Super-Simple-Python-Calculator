#loopable calculator

#Calculator Function
def simpcalc() :
	num1 = float(input("Enter first number: "))
	
	print("Operator examples : (+, - , *, /)")
	op = input("Enter an operator: ")
	
	num2 = float(input("Enter your second number: "))

	if op == "+" :
		addition = num1 + num2
		print(addition)
		
	elif op == "-" :
		subtraction = num1 - num2
		print(subtraction) 
		
	elif op == "/" :
		if num1 or num2 == 0:
			num1 = int(num1)
			num2 = int(num2)
			division = num1 / num2
		else:
			division = num1 / num2
			print(division)
	
	elif op == "*" :
		multiplication = num1 * num2
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
		return
		
	else:
		print("Invalid answer, please try again")
		loopcalc()
		
#calling the function
simpcalc()