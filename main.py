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