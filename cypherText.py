'''
When typing in a message to encrypted or decrypted use lower case and no spaces!
'''

MAPPING = {
    'A': 'N',
    'B': 'O',
    'C': 'P',
    'D': 'Q',
    'E': 'R',
    'F': 'S',
    'G': 'T',
    'H': 'U',
    'I': 'V',
    'J': 'W',
    'K': 'X',
    'L': 'Y',
    'M': 'Z',
    'N': 'A',
    'O': 'B',
    'P': 'C',
    'Q': 'D',
    'R': 'E',
    'S': 'F',
    'T': 'G',
    'U': 'H',
    'V': 'I',
    'W': 'J',
    'X': 'K',
    'Y': 'L',
    'Z': 'M',
}

def cipher(original):
    text = " "
    for letter in original:
        letter = letter.upper()
        new_letter = MAPPING[letter]
        text = text + new_letter
    return text

text = input("Enter text to be ciphered: ")
result = cipher(text)
print(result)    