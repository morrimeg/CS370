## One Time Password App

**Background Information:** <br>
-This QR code works on Android. I was not able to test it on iOS.
-Runs in Python3
-Uses the modules qrcode and pyotp. You may need to install both of these modules:
	pip3 install qrcode
	pip3 install pyotp

<br>
**Running the Program:** <br>
In order to run this program, you must run it in the following way:

1. Run the following command in the command line:
	python3 submission.py --generate-qr

2. Now run the following command in the command line:
	python3 submission.py --get-otp

<br>
You MUST run --generate-qr BEFORE running -get-otp. Otherwise you will recieve and error and no QR code will be generated. The secret key and AR code need to be generated from the --generate-qr first as this secrety key is shared with the function that is run with --get-otp, which is how the TOTP is generated and the QR code is how the TOTP will be accessed. 

<br>
Once you run --generate-qr, a jpg with the QR code will be saved wherever you run this python file. The file where the QR code is saved is called: ga_qr_code.jpg. --generate-qr creates a Google Authenticator URI and turns it into a QR code, which can be scanned into the Google Authenticator app.

<br>
In order to test the TOTP, you will need to open the ga_qr_code.png image and scan this into the Google Authenticator Android app. Then, a TOTP will be generated in the Google Authenticator App.

<br>
You can cross check the Google Authenticator generated TOTP with the TOTP that is output to the terminal after running --get-otp. 

<br>
**Information about my code:** <br>

The nice thing about pyotp is that it does most of the heavy lifting as far as generating uri's and secret keys for TOTP. 

The code contains two functions, generate_qr_code() and generate_otp().

The generate_qr_code() function uses pyotp's random_base32() function which is used to generate a random key. This key is then used in pyotp's TOTP function, along with the user's account information. These bits of information are used to generate a uri in a QR code which can be used in Google Authenticator.

The generate_otp() function takes in the secret key that was generated from the generate_qr_code() function to produce the 6-digit TOTP number that you can see in the Google Authenticator app. Sharing the secret is the biggest thing that needs to happen bewtween the two functions, otherwise the QR code would not be linked up correctly. This function also outputs the 6-digit TOTP number. This number will change every 30 seconds and will match the 6-digit number that appears in your Google Authenticator app.


