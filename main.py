alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

is_over = False
while not is_over:
    direction = input("Write 'encode' if you wanna encrypt, and 'decode' if you wanna decrypt:  ")
    text = input("Write a message:  ").lower()
    shift = int(input("Write a shift number:  ")) % 26

    end_text = ""
    if direction == "decode":
        shift *= -1
    for character in text:
        if character in alphabet:
            character_position = alphabet.index(character)
            new_character_position = character_position + shift
            end_text += alphabet[new_character_position]
        else:
            end_text += character
    print(end_text)
    restart = input("Do you wanna go again?  ")
    if restart == "no":
        is_over = True
        print("Goodbye! :D")
