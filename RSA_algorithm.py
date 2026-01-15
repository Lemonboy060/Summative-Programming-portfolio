from tkinter import *
from tkinter import messagebox
import random

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

        Label(self.parent_frame, text = "Encrypted String: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=160)
        Label(self.parent_frame, text = "Decrypted String: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=200)

        self.encrypt_button = Button(self.parent_frame, text="Encrypt", font = (20), command=self.encrpyt)
        self.encrypt_button.place(x = 175, y = 255)
        self.decrypt_button = Button(self.parent_frame, text="Decrypt", font = (20), command=self.decrypt)
        self.decrypt_button.place(x = 260, y = 255)

        self.encrypt_button["state"] = "disabled"
        self.decrypt_button["state"] = "disabled"

        Button(self.parent_frame, text="Generate keys", font = (20), command=self.rsa_menu).place(x = 340, y = 255)

    def rsa_menu(self):
        self.plaintext = self.entry.get()
        self.pub_key = self.entry_public_key.get()
        self.pri_key = self.entry_private_key.get()

        if self.plaintext == "":
            messagebox.showerror("Error", "Please enter plaintext")
            return

        if self.pub_key == "" and self.pri_key == "":
            self.pub_key, self.pri_key, self.prime_product = self.generate_keys()
        elif len(self.pub_key) > 0 and len(self.pri_key) > 0:
            messagebox.showerror("Error", "Please enter valid key")
            return
        else:
            messagebox.showerror("Error", "Please enter values for both keys or none to generate keys")
            return 
        
        self.encrypt_button["state"] = "normal"
        self.decrypt_button["state"] = "normal"
        

    
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
        min_prime = 101
        max_prime = 10007

        valid_prime1 = False
        valid_prime2 = False
        while valid_prime1 == False:
            prime1 = random.randint(min_prime, max_prime)
            valid_prime1 = self.is_prime(prime1)

        while valid_prime2 == False:
            prime2 = random.randint(min_prime, max_prime)
            valid_prime2 = self.is_prime(prime2)

        prime_product = prime1*prime2
        prime_totient = (prime1-1) * (prime2-1)
              
        valid_public_key = False
        while valid_public_key == False:
            public_key = random.randint(min_prime, max_prime)
            valid_public_key = self.check_public_key(prime_totient, public_key)

        private_key = pow(public_key, -1, prime_totient)
        
        # if valid_public_key == True:
        #     print(f"Prime 1: {prime1}")
        #     print(f"Prime 2: {prime2}")    
        #     print(f"Totient: {prime_totient}")
        #     print(f"Public key: {public_key}")
        #     print(f"Private key: {private_key}")

        return public_key, private_key, prime_product
    

    def is_prime(self, num_check):
        for i_index in range(2, num_check):
            if num_check % i_index == 0:
                return False
        return True
    
    def check_public_key(self, totient, public_key):
        factor_totient = totient % public_key
        if public_key > totient:
            return False
        if self.is_prime(public_key) == False:
            return False
        if factor_totient == 0:
            return False
        return True
        
        
    def divide_string(self, word):
        word_array = []
        ascii_array = []
        for letter in word:
            word_array.append(letter)

        for letter in word_array:
            ascii_array.append(ord(letter))

        return ascii_array
        
    
    def encrpyt(self):
        """
        Used public key to encrypt the message 
        
        to encrypt the message, the message value must be raised by the public key, then modded
        by the product of the primes, to get the cipher text

        Both encyption and decryption can also be done when swapping the key values

        message^B mod N = cipher
        """
        self.encrypted_array = []
        plaintext_ascii = self.divide_string(self.plaintext)

        for value in plaintext_ascii:
            self.encrypted_array.append(pow(value, self.pri_key, self.prime_product))

        encypted_plaintext = "".join(str(str_value) for str_value in self.encrypted_array)

        encryption = Label(self.parent_frame, text = f"{encypted_plaintext}", bg = "Light Blue", font = (20), fg = "black")
        encryption.place(x=140, y=160)

        self.encrypt_button["state"] = "disabled"
    
    def decrypt(self):
        """
        uses private key to decrpyt the message

        to decrypt the message, the cipher text value must be raised by the private key, then modded
        by the product of the primes, to get the cipher text

        Both encyption and decryption can also be done when swapping the key values
        
        Cipher^I mod N = message
        """
        self.decypted_ascii_values = []
        self.decypted_values = []

        for value in self.encrypted_array:
            self.decypted_ascii_values.append(pow(value, self.pub_key, self.prime_product))
        
        for value in self.decypted_ascii_values:
            self.decypted_values.append(chr(value))

        original_plaintext = ", ".join(self.decypted_values)

        original = Label(self.parent_frame, text = f"{original_plaintext}", bg = "Light Blue", font = (20), fg = "black")
        original.place(x=140, y=200)

        self.decrypt_button["state"] = "disabled"
