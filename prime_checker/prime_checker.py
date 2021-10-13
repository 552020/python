# Dirty Version 
def prime_checker(number):
	if (number % 1 == 0) and (number % number == 0):
		check_list = []
		for prev_number in range(2, number):
			if (number % prev_number == 0 ):
				check_list.append(prev_number)
			
		if len(check_list) == 0:
			print('It\'s a prime number.')
		else:
			print('This is not a prime number.')
	else:
		print('This is not a prime number.')


n = int(input("Check this number: "))
prime_checker(number=n)

# Cleaner Version

def clean_prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's clear a prime number! 🙌🏼")
    else:
        print('It\'s clear not a prime number. 👎🏼')

clean_prime_checker(number=n)