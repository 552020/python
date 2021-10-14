# my dirty version

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if shift > len(alphabet):
	shift = shift % len(alphabet)

def caesar(entered_text, entered_shift, entered_direction):
    output_word = []
    for letter in entered_text:
        if letter not in alphabet:
            output_word.append(letter)
    else:
        index = alphabet.index(letter)
        if entered_direction == 'encode':
            if alphabet.index(letter) + entered_shift <= len(alphabet) \
                - 1:
                output_word.append(alphabet[index + entered_shift])
            else:
                output_word.append(alphabet[index + entered_shift
                                   - len(alphabet)])
        if entered_direction == 'decode':
            output_word.append(alphabet[index - entered_shift])

    print(''.join(output_word))

def cipher():
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))

	if shift > len(alphabet):
		shift = shift % len(alphabet)

	caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

want_cipher = False

def ask_user():
    cipher_again = \
        input('Do you want to cipher or decipher another message? Plase type "yes" or "no"'
              )
    if cipher_again == 'yes':
        global want_cipher
        want_cipher = True
    else:
      want_cipher = False
      print('See you! 👋🏼')

cipher()
ask_user()

while want_cipher:
	cipher()
	ask_user()

# angela's version

# from art import logo

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for char in start_text:
    
#     if char not in alphabet:
# 	    end_text += char
#     if char in alphabet: 
# 	    position = alphabet.index(char)
# 	    new_position = position + shift_amount
# 	    end_text += alphabet[new_position]
		
#   print(f"Here's the {cipher_direction}d result: {end_text}")


# print(logo)


# def cipher():
# 	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# 	text = input("Type your message:\n").lower()
# 	shift = int(input("Type the shift number:\n"))

# 	if shift > len(alphabet):
# 		shift = shift % len(alphabet)

# 	caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

# want_cipher = False

# def ask_user():
#     global want_cipher 
#     cipher_again = input('Do you want to cipher or decipher another message? Plase type "yes" or "no": \n')
#     if cipher_again == "yes":
# 	    want_cipher = True
#     else: 
#         want_cipher = False
#         print('See you! 👋🏼')
		
# cipher()
# ask_user()

# while want_cipher:
# 	cipher()
# 	ask_user()