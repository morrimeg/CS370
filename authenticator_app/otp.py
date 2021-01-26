## Name: Megan Morrison
## Date: November 25, 2020
## Course: CS 370
## Assignment: Assignment 2
## Description: The submission.py file first creates a uri which is implemented into
##              a QR code which can be used with the Google Authenticator app. Then,
##              the user can compare the 6-digit TOTP that is output from the
##              generate_otp() function with the 6-digit TOTP that is in the
##              Google Authenticator app. This code will change every 30 seconds.

## References:
## QR Code code:
## https://codeburst.io/how-to-create-your-own-qr-code-programmatically-7b7290252b15
## https://github.com/lincolnloop/python-qrcode

## Google Authenticator info:
## https://stackoverflow.com/questions/8529265/google-authenticator-implementation-in-python
## https://hackernoon.com/how-to-implement-google-authenticator-two-factor-auth-in-javascript-091wy3vh3
## https://pyauth.github.io/pyotp/

# Libraries needed
import qrcode
import pyotp
import sys


def generate_qr_code():
    """
    The generate_qr_code function creates a google uri which is
    placed into a QR code, which can be used with the Google
    Authenticator Android App. The QR code image is saved as
    ga_qr_code.jpg.
    :return: None
    """

    # Create a file to store the user's unique key
    user_key_file = open("./user_key", "w")

    # Randomly generate a random secret
    secret_key = pyotp.random_base32()

    # Write secret key to the key file
    user_key_file.write(secret_key)

    # Close file
    user_key_file.close()

    # Create the uri which will be used to generate the QR Code
    ga_uri = pyotp.totp.TOTP(secret_key).provisioning_uri(name='alice@google.com', issuer_name='Secure App')

    # Generate the QR Code
    qrcode.make(ga_uri).save("./ga_qr_code.jpg")

    # Let user know QR code was generated and the file name
    print("Success: QR Code generated and saved as ./ga_qr_code.jpg")


def generate_totp():
    """
    The generate_totp function takes in the user's secret that is
    created in the generate_qr_code function and prints out the
    current TOTP. The TOTP that is printed will be the same TOTP
    that is seen in the Google Authenticator Android app and can
    be checked once the QR code is added to Google Authenticator.
    :return:
    """

    # Open the file with the secret key
    try:
        keyfile = open("./user_key", "r")

    # If file does not exist, let user know
    except:
        print("Failed to load Secret Key File. Please run " + sys.argv[
            0] + " --generate-qr \nto generate a QR and corresponding secret key file.")
        exit()

    # Get the secret key from the file
    key = keyfile.readlines()

    # Remove newline at end of file
    key = key[0].replace("\n", "")

    # Get the TOTP
    totp = pyotp.TOTP(key)

    # Print the current TOTP
    print("Current OTP:", totp.now())



if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Insufficient Arguments Provided. Quitting.")
        exit()
    if sys.argv[1] == "--generate-qr":
        generate_qr_code()
        exit()
    elif sys.argv[1] == "--get-otp":
        generate_totp()
        exit()
    else:
        print("Incorrect Argument(s) Provided. Quitting.")
        exit()