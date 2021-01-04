### Caesar Cipher
###

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)


# function that enables one of the modes 'encrypt', 'decrypt', or 'hack':
def getMode():
    while True:
        print('Do you wish to encrypt, decrypt or hack a sessage?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd', 'hack', 'h']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "hack" or "h".')


# function for outputting a message
def getMessage():
    print('Enter your message:')
    return input()


# getting a key for the cipher
def getKey():
    key = 0
    while True:
        print('Enter the Key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key


# function for decrypting
def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:

            translated += symbol
        else:

            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]
    return translated


mode = getMode()
message = getMessage()
if mode[0] != 'h':
    key = getKey()
print('Translated chipher:')
if mode[0] != 'h':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage(mode, message, key))
