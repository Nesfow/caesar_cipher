# caesar_cipher
Simple Caesar Cipher in Python

Tool to decrypt/encrypt with Caesar. Caesar cipher (or Caesar code) is a shift cipher, one of the most easy and most famous encryption systems. It uses the substitution of a letter by another one further in the alphabet.

Encryption with Caesar code is based on an alphabet shift (move of letters further in the alphabet), it is a monoalphabetical substitution cipher, ie. a same letter is replaced with only one other (always the same for given cipher message). The most commonly used shift/offset is by 3 letters.

Example: Crypt DCODEX with a shift of 3.
To encrypt D, take the alphabet and look 3 letters after: G. So D is encrypted with G.
To encrypt X, loop the alphabet: after X : Y, after Y : Z, after Z : A. So X is coded A.
DCODEX is coded GFRGHA

Caesar code decryption replaces a letter another with an inverse alphabet shift: a previous letter in the alphabet.

Example: Decrypt GFRGHA with a shift of 3.
To decrypt G, take the alphabet and look 3 letters before: D. So G is decrypted with D.
To decrypt X, loop the alphabet: before A: Z, before Z: Y, before Y: X. So A is decrypted X.
GFRGHA is decrypted DCODEX.
