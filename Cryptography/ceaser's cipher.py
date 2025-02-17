import string

def encrypt_message(input):
    encrypted_message = ""
    for i in range(len(input)):
        if input[i] in string.whitespace or input[i] in string.punctuation:
            encrypted_message = encrypted_message + input[i]
        else:
            pos = (string.ascii_lowercase.find(input[i]) + caesers_shift) % 26
            encrypted_message = encrypted_message + string.ascii_lowercase[pos]
    return encrypted_message

def decrypt_message(input):
    decrypted_message = ""
    for i in range(len(input)):
        if input[i] in string.whitespace or input[i] in string.punctuation:
            decrypted_message = decrypted_message + input[i]
        else:
            pos = (string.ascii_lowercase.find(input[i]) - caesers_shift) % 26
            decrypted_message = decrypted_message + string.ascii_lowercase[pos]
    return decrypted_message


caesers_shift = 5

while True:
    user_option = input("Do you want to encrypt or decrypt a message? (e/d): ")
    if user_option == "e":
        user_input = input("Write the message you want encoded: ")
        lc_input = user_input.lower()
        print(encrypt_message(lc_input))
    elif user_option == "d":
        user_input = input("Write the message you want decoded: ")
        lc_input = user_input.lower()
        print(decrypt_message(lc_input))
    else:
        print("Invalid input. Please try again.")

