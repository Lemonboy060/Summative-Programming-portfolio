from tkinter import *

class RSA():
    def __init__(self, parent_frame):     
        self.parent_frame = parent_frame
        Label(self.parent_frame, text = "Enter string to encrypt: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=40)
        self.entry = Entry(parent_frame, width=35)
        self.entry.place(x = 202, y = 42)
        Label(self.parent_frame, text = "Enter Public Key: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=80)
        self.entry_public_key = Entry(parent_frame, width=35)
        self.entry_public_key.place(x = 202, y = 82)
        Label(self.parent_frame, text = "Enter Private Key: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=120)
        self.entry_private_key = Entry(parent_frame, width=35)
        self.entry_private_key.place(x = 202, y = 122)

        Label(self.parent_frame, text = "Outputted Text: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=160)

        Button(self.parent_frame, text="Encrypt", font = (20), command=self.rsa_menu).place(x = 175, y = 195)
        Button(self.parent_frame, text="Decrypt", font = (20)).place(x = 260, y = 195)

    def rsa_menu(self):
        pub_key = self.entry_public_key.get()
        pri_key = self.entry_private_key.get()

        print(pub_key, pri_key)
    
    def generate_keys(self):
        """
        Used to generate both the public and private keys for enrypting and decrypting
        user strings

        To genertate keys
            - Select two prime number, P1 and P2
            - Calculate the product of thsoe primes N = p1 x p2
            - Calculate the Totient of those primes T = (p1-1) x (p2-1)
        
        Then to select public key (B), select a random number
            - Number must be prime
            - be less then the totient B < T
            - must not be a factor of the totient, T mod B != 0

        Then to select private key (I), select random number
            - Product of I (private) and B (public) divided by the totient must have a remainder of 1
            so (B x I) mod T = 1    
        :param self: Description
        """
    
    def encrpyt(self):
        """
        Used public key to encrypt the message 
        
        to encrypt the message, the message value must be raised by the public key, then modded
        by the product of the primes, to get the cipher text

        Both encyption and decryption can also be done when swapping the key values

        message^B mod N = cipher
        """
    
    def decrypt(self):
        """
        uses private key to decrpyt the message

        to decrypt the message, the cipher text value must be raised by the private key, then modded
        by the product of the primes, to get the cipher text

        Both encyption and decryption can also be done when swapping the key values
        
        Cipher^I mod N = message
        """