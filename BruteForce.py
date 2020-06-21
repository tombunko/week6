#!/usr/bin/python3

import hashlib
from itertools import chain, product
from datetime import datetime
starttime = ""

#hash the real password - realHash

def bruteforce(charset, minlength, maxlength):
        return (''.join(candidate)                                      # joins all items into a string

        for candidate in chain.from_iterable(product(charset, repeat=i) # Construct the bruteforce string
        for i in range(minlength, maxlength + 1)))                      # to compare the string to

def checkPass(charinput, minlength, maxlength, realpass):
        starttime = datetime.now()                                      # record the start time
        realhash = hashlib.sha256(realpass.encode("utf-8")).hexdigest() # hash the real password - realHash
        print("The hashed real password is: ", realhash)                # advise what we are looking for

        for attempt in bruteforce(charinput, minlength, maxlength):
                attempthash = hashlib.sha256(attempt.encode("utf-8")).hexdigest()   # hash the guess
                if attempthash == realhash:                                         # does guess = real one?
                        print("Password has been cracked! It is : " + realpass)     # advise password cracked
                        timeTaken = datetime.now() - starttime                      # calc time to crack
                        print("Time taken to calculate: ", timeTaken)               # advise time to crack
                        break                                                       # terminate program



# charinput contains all the characters we use on the brute force

charinput = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
minlen = int(input("Enter the Minimum Length of the password to search for: "))
maxlen = int(input("Enter the Maximum Length of the password to search for: "))
realpass = input("Enter the Password that we are going to try to break: ")

print(checkPass(charinput,minlen,maxlen,realpass))


