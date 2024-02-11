import string
def make_list(character_length,characters):
    counter = 0 
    with open("wordlist.txt", "w") as file_open:
        for length in range(character_length, character_length + 1):
            for i in range(len(characters) ** length):
                password = ""
                num = i 
                for _ in range(length):
                    password = characters[num % len(characters)] + password
                    num //= len(characters)
                file_open.write(password + "\n")
                counter += 1
    print(f"Wordlist of {counter} passwords has been generated!")

character_length = input("Enter the length of the password>>")
while True:
    if character_length.isdigit():
        character_length = int(character_length)
        if character_length > 0 :
            break
        else:
            print("Invalid input. Please enter a positive integer.")
            character_length = input("Enter the length of the password>>")
        break
    else:
        print("Invalid input. Please enter a valid input.")
        character_length = input("Enter the length of the password>>")


characters = ""
main_cmd = input("""
PassBuilder
Type 1, For predefined characters
Type 2, For custom characters
""")

while True:
    if main_cmd == "1":

        cmd = input("Wanna use lower case letters? (y/n)>>")
        while True:   
            if cmd == "y":
                characters = string.ascii_lowercase
                break
            elif cmd == "n":
                break
            else:
                print("Enter Valid Input!")
                cmd = input("Wanna use lower case letters? (y/n)>>")

        cmd = input("Wanna use upper case letters? (y/n)>>")
        while True:   
            if cmd == "y":
                characters += string.ascii_uppercase
                break
            elif cmd == "n":
                break
            else:
                print("Enter Valid Input!")
                cmd = input("Wanna use upper case letters? (y/n)>>")
            
        cmd = input("Wanna use digits? (y/n)>>")
        while True:   
            if cmd == "y":
                characters += string.digits
                break
            elif cmd == "n":
                break
            else:
                print("Enter Valid Input!")
                cmd = input("Wanna use digits? (y/n)>>")

        cmd = input("Wanna use special characters? (y/n)>>")
        while True:
            if cmd == "y":
                special_characters = input("Enter the special characters>>")
                characters += special_characters
                break
            elif cmd == "n":
                break
            else:
                print("Enter Valid Input!")
                cmd = input("Wanna use special characters? (y/n)>>")

        break

    elif main_cmd == "2":
        characters = input("Enter all the characters for the wordlist>>")
        break

    else:
        main_cmd = input("""
        Enter Valid Input
        Type 1, For predefined characters
        Type 2, For custom characters
        """)
    
print(characters)

make_list(character_length,characters)