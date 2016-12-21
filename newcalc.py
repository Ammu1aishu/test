try:
	number_1 = int(input('Please enter the first number: '))
	number_2 = int(input('Please enter the second number: '))
	#def calculate():
	operation = raw_input("Please type in the math operation you would like to complete:")
	if operation == '+':
        	print('{} + {} = '.format(number_1, number_2))
        	print(number_1 + number_2)

	elif operation == '-':
        	print('{} - {} = '.format(number_1, number_2))
        	print(number_1 - number_2)

	elif operation == '*':
        	print('{} * {} = '.format(number_1, number_2))
        	print(number_1 * number_2)

	elif operation == '/':
        	print('{} / {} = '.format(number_1, number_2))
        	print(number_1 / number_2)
	else:
		print("invalid operator.")
except ArithmeticError as err:
	print("you are entering the invalid operator")
