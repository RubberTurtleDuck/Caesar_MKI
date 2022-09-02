alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, shift):
    encrypted_text = ""
    for letter in message:
        if letter == " ":
            shifted_letter = " "
            encrypted_text += shifted_letter
        else:
            index = (letter_to_index[letter]) + shift % len(alphabet)
            shifted_letter = index_to_letter[index]
            encrypted_text += shifted_letter
    return encrypted_text


def decrypt(ciphered_text, shift):
    decrypted_text = ""
    for letter in ciphered_text:
        if letter == " ":
            unshifted_letter = " "
            decrypted_text += unshifted_letter
        else:
            index = (letter_to_index[letter]) - shift % len(alphabet)
            shifted_letter = index_to_letter[index]
            decrypted_text += shifted_letter
    return decrypted_text


on = True
while on:
    user_choice = input("E encrypt message. / D to decrypt message. / Write 'exit' to close the program: ").lower()

    if user_choice == "e":
        text = input("Write the message you want to encrypt: ").lower()
        shift_number = int(input("Write how many slots you want to shift the cipher: "))
        encrypted_message = encrypt(text, shift_number)
        print(encrypted_message)
    elif user_choice == "d":
        text = input("Write the message you want to decrypt: ").lower()
        shift_number = int(input("Write how many slots you want to shift the cipher: "))
        encrypted_message = decrypt(text, shift_number)
        print(encrypted_message)
    elif user_choice == "exit":
        on = False
