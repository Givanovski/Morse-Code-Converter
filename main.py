class MorseCodeConverter:
    """Class for converting text to Morse code and vice versa."""

    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', '0': '-----', " ": "|"
    }

    def text_to_morse(self, message):
        """
        Convert a given text message to Morse code.

        Parameters:
        - message (str): The text message to convert.

        Returns:
        - str: The Morse code representation of the input text.
        """
        morse_code = " ".join(self.morse_code_dict[char.upper()] for char in message)
        return morse_code

    def morse_to_text(self, message):
        """
        Convert a given Morse code message to text.

        Parameters:
        - message (str): The Morse code message to convert.

        Returns:
        - str: The text representation of the input Morse code.
        """
        reverse_morse_code_dict = {value: key for key, value in self.morse_code_dict.items()}
        morse_code_elements = message.split(" ")
        text_message = "".join(
            reverse_morse_code_dict[element] if element in reverse_morse_code_dict else " " for element in
            morse_code_elements)
        return text_message

    def main(self):
        """
        Main function to interactively use the MorseCodeConverter.

        The function provides a command-line interface for the user to choose
        between converting text to Morse code, Morse code to text, or quitting the program.
        """
        while True:
            choice = input(
                "Choose an option:\n1. Text to Morse Code\n2. Morse Code to Text\n3. Quit\nEnter choice (1/2/3): ")

            if choice == "1":
                message = input("Enter a string: ")
                morse_result = self.text_to_morse(message)
                print(f"Morse Code: {morse_result}")
            elif choice == "2":
                message = input("Enter Morse code: ")
                text_result = self.morse_to_text(message)
                print(f"Translated Text: {text_result}")
            elif choice == "3":
                print("Exiting the Morse Code game. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    morse_converter = MorseCodeConverter()
    morse_converter.main()
