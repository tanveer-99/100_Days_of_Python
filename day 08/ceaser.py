from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(logo)


def ceaser(direction, message, shift_number):

    output = ""
    if direction == "decrypt":
        shift_number = -shift_number


    for letter in message:
        if letter not in message:
            output += letter
        else:
            new_position = alphabet.index(letter) + shift_number
            new_position = new_position % 26
            shifted_letter = alphabet[new_position]
            output += shifted_letter

    print(f"Here's the {direction}d result: {output}")

repeat_process = True
while repeat_process:
    direction = input("Type 'encrypt' to encrypt, type 'decrypt' to decrypt: ").lower()
    # what if someone types incorrectly!
    message = input("Type your message: ").lower()
    shift_number = int(input("Type the shift number: "))

    ceaser(direction, message, shift_number)

    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if repeat == 'no':
        print("GoodBye!")
        repeat_process = False



