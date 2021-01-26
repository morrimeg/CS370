## Name: Megan Morrison
## Date: 10-13-2020
## Class: CS370
## Assignment: Programming Assignment 1, Problem 3.4
## Description: This file contains functions which encrypt
##              a given plaintext file based off of a key which
##              is a word from an English dictionary. The script
##              then matches the given ciphertext to the encrypted
##              ciphertext to see if the word used as the key is found.
##              If the key is found, it is reported.


from Crypto.Cipher import AES  #Works
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def read_english_words(filename):
    """The function read_english_words takes in the name
        and extention of a file that pertains to a dictionary of English
        words and copies each word into a list.
    """

    try:
        # empty list to hold dictionary of words
        english_words_list = []

        # Open the file that is given
        with open(filename, 'r') as infile:

            # Got this code to create a list of lists
            # from the following:
            #  https://www.kite.com/python/answers/how-to-convert-each-line-in-a-text-file-into-a-list-in-python

            english_words_list = [(line.strip()) for line in infile]

        # If the file is not found, let the user know by raising the FileNotFound
        # exception
    except FileNotFoundError:
        print("The file was not found.")

        # If the file is found, then get the sum of our numbers and
        # output this sum to a text file.
    else:
        return english_words_list



def pad_word(english_word, spaces_needed):
    """
        The function pad_word takes in the
        current word and pads it so that it
        is 16 characters in length. It returns
        the padded word
    """

    # Pad end of word with spaces as needed
    for i in range(0, spaces_needed):
        english_word = english_word + ' '

    return english_word



def encryption_encodings(key_value):
    """
        The function encryption_encodings takes in the
        padded key. This function encodes the key as
        well as the iv that is to be used. The encoded
        key and iv are returned.
    """

    # This code is from the pycryptodome documentation
    # https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html?highlight=cbc#cbc-mode
    key_bytes = bytearray(key_value, encoding="utf-8")

    # Get the iv for the encryption
    iv = bytearray.fromhex("00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")

    return key_bytes, iv


def encrypt_message(key, iv, plaintext):
    """
        The encrypt_message function takes in the padded
        key, iv, and plaintext. It then encrypts the plaintext
        using the key and iv. The encrypted ciphertext is
        returned.
    """

    # Create new encryption scheme. AES-128-CBC is used here
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Encrypt the message
    ct_bytes = cipher.encrypt(pad(str.encode(plaintext), AES.block_size))

    # figured out how to convert bytes to hex from:
    # https://www.kite.com/python/answers/how-to-convert-bytes-to-a-hexadecimal-string-in-python
    encrypted_ciphertext = ct_bytes.hex()

    return encrypted_ciphertext




def find_word(words_list, plaintext, ciphertext):
    """ The function find_word takes in the words list, plaintext,
        and ciphertext that is given. It searches the word list for
        words less than 16 in length, and then encrypts the word.
        Finally, the encrpyted ciphertext is compared with the given
        ciphertext. If a match is found, the word is returned.
    """

    found_word = '' # variable to hold the word that matches the ciphertext

    # Itereate through words list
    for word in words_list:

        # Find words that are less than 16 in length
        if(len(word) < 16):

            # Get the current word's length
            current_word_length = len(word)

            # Get how many spaces are needed to make it
            # a word that has a length of 16
            spaces_needed = 16 - current_word_length

            # Pad the word to get the 16-bit key
            key = pad_word(word, spaces_needed)

            # Encode the key and iv to correct values (e.g. utf-8 or hex)
            key_bytes, iv = encryption_encodings(key)

            # Encrypt the message
            ciphertext_encrypted = encrypt_message(key_bytes, iv, plaintext)

            # See if generated ciphertext matches given ciphertext
            if(ciphertext == ciphertext_encrypted):

                # Set the found word
                found_word = word
                break

        # Otherwise continue on to the next word in the list
        else:
            continue

    return found_word



def main():
    # Read in English words list
    english_words = read_english_words('english_words.txt')

    # Ciphertext string
    ciphertext =  '8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9'

    # Plaintext string
    plaintext = 'This is a top secret.'

    # find the word!
    the_key = find_word(english_words, plaintext, ciphertext)

    # Report what the key is!
    if len(the_key) != 0:
        print("the key is...", the_key)

    else:
        print("The key was not found.")


main()




