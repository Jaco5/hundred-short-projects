def encrypt(text, seed):
    encryptedStr = ""
    switch = True
    for ch in text:
        if ch.isalpha():
            if switch:
                new_ch = ord(ch) + int(seed[0])
                switch = False
            else:
                new_ch = ord(ch) + int(seed[1])
                switch = True
            if new_ch > ord('z'):
                new_ch -= 26
            ch = chr(new_ch)
        encryptedStr += ch
    print(encryptedStr)

def decrypt(text, seed):
    decryptedStr = ""
    switch = True
    for ch in text:
        if ch.isalpha():
            if switch:
                new_ch = ord(ch) - int(seed[0])
                switch = False
            else:
                new_ch = ord(ch) - int(seed[1])
                switch = True
            if new_ch < ord('a'):
                new_ch += 26
            ch = chr(new_ch)
        decryptedStr += ch
    print(decryptedStr)
 
textToCipher = input("Message to be encrypted: ")
#if left blank generate random
cipherseed = input("Enter double digit seed: ")

encrypt(textToCipher, cipherseed)

