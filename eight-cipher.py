def encrypt(text, shift):
    cipherText = ""
    for ch in text:
        if ch.isalpha():
            new_ch = ord(ch) + shift
            if new_ch > ord('z'):
                new_ch -= 26
            ch = chr(new_ch)
        cipherText += ch
    print(cipherText)

def decrypt(text, shift):
    decipheredText = ""
    for ch in text:
        if ch.isalpha():
            new_ch = ord(ch) - shift
            if new_ch < ord('a'):
                new_ch += 26
            ch = chr(new_ch)
        decipheredText += ch
    print(decipheredText)
 
textToCipher = input("Message to be encrypted: ")
cipherShift = int(input("Enter single digit seed: "))

encrypt(textToCipher, cipherShift)

