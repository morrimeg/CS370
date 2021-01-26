## Key Finder

The keyfinder program takes in known cipher text, known plain text, and a dictionary of possible keys. Using an AES-128-cbc encryption algorithm, an algorithm was
written to find the key that matches the plaintext that was given. If the key is found, it is output to the terminal.  


**Running the Program:**

- Make sure the file english_words.txt is in the same directory as the Python script. Otherwise you will get an error message. 

- The Python script will automatically read in the english_words.txt file. 

- To run the Python script, use the following command in the command line:  

  python3 key_finder.py
  

- The word will be output to the screen if found
