# Calculator

#Add
def add(n1, n2):
	return n1 + n2

#Subctract
def subtract(n1, n2):
	return n1 - n2
#Multiply
def multiply(n1, n2):
	return n1 * n2
#Divide
def divide(n1, n2):
	return n1 / n2

#Operations
operations = {
	'+': add,
	'-': subtract,
	'*': multiply,
	'/': divide,
	
}

num1 = int(input('What\'s the first number?: '))
num2 = int(input('What\'s the second number?: '))
for operation in operations:
	print(operation)
operation_symbol = input("Pick an operation from the line above: ")
answer = operations[operation_symbol](num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

answer_list = []
answer_list.append(answer)
def last_answer(): 
    if len(answer_list) > 0:
    	return answer_list[-1]

should_continue = True
while should_continue:
	last_result = last_answer()
	should_continue_input = input(f'Type "y" to continue calculating with {last_result}, or type "n" to exit: ')
	
	if should_continue_input == 'y':
		should_continue = True
	else:
		print('Goodbye! 👋🏼')
		break
	
	operation_symbol = input("Pick another operation: ")
	new_num = int(input('What\'s the next number?: '))
	new_answer = operations[operation_symbol](last_result, new_num)
	answer_list.append(new_answer)
	print(answer_list)
	print(f"{last_answer()} {operation_symbol} {new_num} = {new_answer}")
