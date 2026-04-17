import time

morse_code = {
    "A": ".-", "B":"-...", "C":"-.-", "D":"-..", "E":".",
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----',
    ' ': '/'
}


def play_morse(message):
    for char in message.upper():
        if char not in morse_code:
            continue
        
        code = morse_code[char]
        print(f"{char}:{code}")
            
        time.sleep(0.2)
        
        time.sleep(0.5)

message = input("Please, enter a message: ")
play_morse(message)