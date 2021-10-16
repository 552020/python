from art import logo

print(logo)

def calculator():
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

    num1 = float(input('What\'s the first number?: '))
    num2 = float(input('What\'s the second number?: '))
    for operation in operations:
	    print(operation)
    operation_symbol = input("Pick an operation from the line above: ")

    # first try
    # def operation(f_num1, f_num2, f_operation_symbol):
    # 	if f_operation_symbol == '+':
    # 		return add(f_num1, f_num2)
    # 	if f_operation_symbol == '-':
    # 		return subtract(f_num1, f_num2)
    # 	if f_operation_symbol == '*':
    # 		return multiply(f_num1, f_num2)
    # 	if f_operation_symbol == '/':
    # 		return divide(f_num1, f_num2)

    # second try
    # def operation(f_num1, f_num2, f_operation_symbol):
    # 	return operations[operation_symbol](f_num1, f_num2)

    # answer = operation(num1, num2, operation_symbol)

    # one liner
    answer = operations[operation_symbol](num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    answer_list = []
    answer_list.append(answer)
    def last_answer(): 
        return answer_list[-1]

    # operation_symbol = input("Pick another operation: ")
    # num3 = int(input('What\'s the next number?: '))
    # calculation_function = operations[operation_symbol]
    # second_answer = calculation_function(calculation_function(num1, num2), num3)
    # print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

    should_continue = True
    while should_continue:
        last_result = last_answer()
        # print(answer_list)
        # should_continue_input = input(f'Type "y" to continue calculating with {answer_list[-1]}, or type "n" to exit: ')
        should_continue_input = input(f'Type "c" to continue calculating with {last_result}, "n" to start a new operation, or "q" to exit: ')
        
        if should_continue_input == 'c':
            should_continue = True
        elif should_continue_input == 'q':
            print('Goodbye! 👋🏼')
            break

        elif should_continue_input == "n":
            # break # it didn't work.
            calculator()
        else: 
            print('Please type "c", "n" or "q"!')
        operation_symbol = input("Pick another operation: ")
        new_num = float(input('What\'s the next number?: '))
        # answer = operations[operation_symbol](num1, num2)
        new_answer = operations[operation_symbol](last_result, new_num)
        answer_list.append(new_answer)
        print(f"{last_answer()} {operation_symbol} {new_num} = {new_answer}")

calculator()

	