# WordList Generator

Wordlist Generator is a Python program that generates wordlists with passwords of a specific length. It allows you to choose the length of your passwords and the characters you want to put in them.

## Features

- **Flexible Password Length**: Generate wordlists with passwords of any specified length.
- **Custom Character Sets**: Choose from predefined character sets or define your own custom character set to include in the wordlist.
- **Comprehensive Character Options**: Include lowercase letters, uppercase letters, digits, and/or special characters in the generated passwords.
- **Easy-to-Use Interface**: The program prompts you with clear instructions, making it simple to generate customized wordlists.
- **Quick Execution**: Efficiently generates wordlists containing all possible combinations of the selected characters and length.

## Usage

1. **Input Password Length**: Run the script and specify the appropriate password length when requested. Only positive integers are acceptable.

2. **Choose Character Set**: Choose one of the options below::
   - Enter `1` to utilize predetermined character sets.
   - Enter `2` to establish custom character sets.

3. **Predefined Character Sets**: Select whether to generate passwords with lowercase, uppercase, numbers, or special characters.

4. **Custom Character Set**: Enter the characters you want to include in the wordlist.

5. **Generated Wordlist**: Once the script is completed, a wordlist comprising all possible combinations of the given characters and length will be stored in a file named `wordlist.txt`.

## Dependencies

- This script requires Python version 3.x.
- No extra libraries or dependencies are required.

## Example

Suppose you want to create a wordlist of four-character passwords using lowercase letters and digits. Here's how:
1. Run the script.
2. Specify `4` as the password length.
3. Choose the predefined characters option (`1`).
4. Select lowercase letters (`y`) and digits (`y`).
5. After the script finishes running, you'll find the generated wordlist in `wordlist.txt`.