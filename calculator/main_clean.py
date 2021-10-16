from art import logo

print(logo)

def calculator():
    def add(n1, n2):
        return n1 + n2


    def subtract(n1, n2):
        return n1 - n2


    def multiply(n1, n2):
        return n1 * n2


    def divide(n1, n2):
        return n1 / n2


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
    answer = operations[operation_symbol](num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    answer_list = []
    answer_list.append(answer)
    def last_answer(): 
        return answer_list[-1]

    should_continue = True
    while should_continue:
        last_result = last_answer()
        should_continue_input = input(f'Type "c" to continue calculating with {last_result}, "n" to start a new operation, or "q" to exit: ')
        
        if should_continue_input == 'c':
            should_continue = True
        elif should_continue_input == 'q':
            print('Goodbye! 👋🏼')
            break
        elif should_continue_input == "n":
            calculator()
        else: 
            print('Please type "c", "n" or "q"!')
        operation_symbol = input("Pick another operation: ")
        new_num = float(input('What\'s the next number?: '))
        new_answer = operations[operation_symbol](last_result, new_num)
        answer_list.append(new_answer)
        print(f"{last_answer()} {operation_symbol} {new_num} = {new_answer}")

calculator()