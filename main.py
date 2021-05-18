alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift_amount,cipher_direction):
    final_text = ""
    if cipher_direction == "decode":
        shift_amount *=-1
    for char in text:
        if char not in alphabet:
            final_text += char
        else:
            position = alphabet.index(char)
            new_position = (position + shift_amount)%26 # to handle out of boundry index
            final_text += alphabet[new_position]
    
    print(f"Here's the {cipher_direction}d result: {final_text}")

from art import logo
print(logo)
finish = "yes"

while finish == "yes": 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text=text,shift_amount=shift,cipher_direction=direction)
    finish = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    print(finish)

print("Goodbye")


