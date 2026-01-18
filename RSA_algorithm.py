from tkinter import *
from tkinter import messagebox
import random

class RSA():
    def __init__(self, parent_frame, mediator):
        """
        Creates all necessary widgets for the RSA class user interface

        Creates all the necessary entry boxes, lables and buttons for the RSA frame invluding 
        the generate keyts button and validate keys button, to call their respected functions

        Args:
        parent_frame (tkinter.Frame): The class's frame, which will contain all the relevant widgets 
        """     
        self.parent_frame = parent_frame
        self.mediator = mediator
        Label(self.parent_frame, text = "Enter string to encrypt: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=40)
        self.entry = Entry(parent_frame, width=35)
        self.entry.place(x = 202, y = 42)
        Label(self.parent_frame, text = "Enter Public Key: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=80)
        self.entry_public_key = Entry(parent_frame, width=35)
        self.entry_public_key.place(x = 202, y = 82)
        Label(self.parent_frame, text = "Enter Private Key: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=120)
        self.entry_private_key = Entry(parent_frame, width=35)
        self.entry_private_key.place(x = 202, y = 122)
        Label(self.parent_frame, text = "Enter modulus for keys: ", bg = "light blue", font = (20), fg = "black").place(x=450, y=40)
        self.entry_modulus = Entry(parent_frame, width=35)
        self.entry_modulus.place(x =650, y = 42)

        Label(self.parent_frame, text = "Encrypted String: ", bg = "light blue", font = (20), fg = "black").place(x=450, y=80)
        Label(self.parent_frame, text = "Decrypted String: ", bg = "light blue", font = (20), fg = "black").place(x=450, y=120)

        self.encrypt_button = Button(self.parent_frame, text="Encrypt", font = (20), command=self.encrpyt)
        self.encrypt_button.place(x = 175, y = 165)
        self.decrypt_button = Button(self.parent_frame, text="Decrypt", font = (20), command=self.decrypt)
        self.decrypt_button.place(x = 260, y = 165)

        self.mediator.add_buttons("Encrypt_button", self.encrypt_button)
        self.mediator.add_buttons("Decrypt_button", self.decrypt_button)

        self.mediator.disable_button("Encrypt_button")
        self.mediator.disable_button("Decrypt_button")

        self.gen_button = Button(self.parent_frame, text="Generate keys", font = (20), command=self.rsa_menu)
        self.gen_button.place(x = 340, y = 165)
        self.validate_button = Button(self.parent_frame, text="Validate keys", font = (20), command=self.validate_keys)
        self.validate_button.place(x = 465, y = 165)

        self.mediator.add_buttons("Generate_button", self.gen_button)
        self.mediator.add_buttons("Validate_button", self.validate_button)

    def rsa_menu(self):
        """
        rsa_menu function is called when the generate keys button is selected
         
        Acts as a checker, to check whether certain parameter as filled
        in order to generate the keys, if they are not errors boxes are produced

        The menu also calls the generate_keys function to generate the private and public key as
        well as the prime product of the primes seleted during key generation

        Once done, specific buttons are enabled and disabled so the user cannot cause the program to
        break or act incorrectly
        """
        self.plaintext = self.entry.get()
        self.pub_key = self.entry_public_key.get()
        self.pri_key = self.entry_private_key.get()

        if self.plaintext == "":
            messagebox.showerror("Error", "Please enter plaintext")
            return
        if self.pub_key == "" and self.pri_key == "":
            self.pub_key, self.pri_key, self.prime_product = self.generate_keys()
        else:
            messagebox.showerror("Error", "Please enter values for both keys or none to generate keys")
            return 
        
        self.mediator.enable_button("Encrypt_button")
        self.mediator.enable_button("Decrypt_button")
        self.mediator.disable_button("Validate_button")
        
    def validate_keys(self):
        """
        Validate keys function is called when the validate keys button is selected

        The function gets the current values entered into the public and private key entries
        as well as the modulus, which are then tested to see if they are a valid pair of keys
        and modulus

        This is done as, if the keys and modulus did not match, then encrypted text would be produced
        buit when decrypted would output the incorrect plaintext
        """
        self.plaintext = self.entry.get()
        self.pub_key = self.entry_public_key.get()
        self.pri_key = self.entry_private_key.get()
        self.mod = self.entry_modulus.get()

        if self.pub_key.isdigit() == False or self.pri_key.isdigit() == False or self.mod.isdigit() == False:
            messagebox.showerror("Error", "Please ensure both keys and modulus are valid integers")
            return

        if self.plaintext == "":
            messagebox.showerror("Error", "Please enter plaintext")
            return
        if self.pub_key == "" or self.pri_key == "" or self.mod == "":
            messagebox.showerror("Error", "Please enter Public key, private key and modulus")
            return

        test_pub_key = int(self.pub_key)
        test_pri_key = int(self.pri_key)
        test_mod = int(self.mod)

        test_value = 60

        encryp = (pow(test_value, test_pri_key, test_mod))
        decryp = (pow(encryp, test_pub_key, test_mod))

        if decryp == test_value:
            self.valid_keys = True
            self.prime_product = test_mod
            self.pri_key = test_pri_key
            self.pub_key = test_pub_key
            messagebox.showinfo("Valid", "Keys and modulus entered are valid")
            self.mediator.enable_button("Encrypt_button")
            self.mediator.enable_button("Decrypt_button")
            self.mediator.disable_button("Generate_button")

        else:
            self.valid_keys = False
            messagebox.showerror("Error", "Keys and modulus entered are invalid")
            self.mediator.disable_button("Encrypt_button")
            self.mediator.disable_button("Decrypt_button")

    
    def generate_keys(self):
        """
        Used to generate both the public and private keys for enrypting and decrypting
        user plaintext.

        To genertate keys:
            - Select two prime number, P1 and P2
            - Calculate the product of thsoe primes N = p1 x p2
            - Calculate the Totient of those primes T = (p1-1) x (p2-1)
        
        Then to select public key (B), select a random number:
            - Number must be prime
            - be less then the totient B < T
            - must not be a factor of the totient, T mod B != 0

        Then to select private key (I), select random number:
            - Product of I (private) and B (public) divided by the totient must have a remainder of 1
            so (B x I) mod T = 1    
            
        Returns:
        public_key (int): Valid public key randomly generated
        private_key (int): Valid public key randomly generated
        prime_product (int): Product of the two random primes

        This video was used for the basis of my understanind for RSA:
        https://www.youtube.com/watch?v=Pq8gNbvfaoM&list=LL
        """
        min_prime = 101
        max_prime = 5003

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
        return public_key, private_key, prime_product
    

    def is_prime(self, num_check):
        """
        Subfunction used to check whether a number is prime or not

        Args:
        num_check (int): The value to check if its prime or not

        Returns:
        bool: Represents if the integer parameter is prime or not
        """
        for i_index in range(2, num_check):
            if num_check % i_index == 0:
                return False
        return True
    
    def check_public_key(self, totient, public_key):
        """
        Checks specific conditions against the public key to see if the public key is valid
        or not

        for the key to be valid it must not be greater then the totitent, must be prime and 
        must not be a factor of the totient

        if all conditions are met then the public key is valid
        
        Args:
        totient (int): The totient of the the tow primes produced in the generate_keys function
        public_key (int): The value of the public_key being tested

        Returns:
        bool: Represents if the key is public or not
        """
        factor_totient = totient % public_key
        if public_key > totient:
            return False
        if self.is_prime(public_key) == False:
            return False
        if factor_totient == 0:
            return False
        return True
        
        
    def divide_string(self, word):
        """
        Divides the users plaintext in seperate ascii values so that the public or private keys
        can be applied to it
        
        Args:
        word (string): Users plaintext

        Returns:
        ascii_array (list): list of all letters in word parameter, now seprate and in their ascii form
        """
        word_array = []
        ascii_array = []
        for letter in word:
            word_array.append(letter)

        for letter in word_array:
            ascii_array.append(ord(letter))

        return ascii_array
        
    
    def encrpyt(self):
        """
        Uses public key to encrypt the message as well as the product of the primes used earlier
        to calculate the totient  
        
        to encrypt the message, the message value must be raised by the public key, then modded
        by the product of the primes, to get the cipher text

        message^pri_key mod prime_product = cipher_text
        """
        self.encrypted_array = []
        plaintext_ascii = self.divide_string(self.plaintext)

        for value in plaintext_ascii:
            self.encrypted_array.append(self.power_value(value, self.pri_key, self.prime_product))

        encypted_plaintext = "".join(str(str_value) for str_value in self.encrypted_array)

        encryption = Label(self.parent_frame, text = f"{encypted_plaintext}", bg = "Light Blue", font = (20), fg = "black")
        encryption.place(x=600, y=80)

        self.mediator.disable_button("Encrypt_button")
    
    def decrypt(self):
        """
        Uses the private key to decrpyt the message

        To decrypt the message, the cipher text value must be raised by the private key, then modded
        by the product of the primes (modulus), to get the cipher text

        Once decypted the plaintext is combined with each character to reassemble the orginal message
        
        Cipher^pub_key mod prime_product = message
        """
        self.decypted_ascii_values = []
        self.decypted_values = []

        for value in self.encrypted_array:
            self.decypted_ascii_values.append(self.power_value(value, self.pub_key, self.prime_product))
        
        for value in self.decypted_ascii_values:
            self.decypted_values.append(chr(value))

        original_plaintext = "".join(self.decypted_values)

        original = Label(self.parent_frame, text = f"{original_plaintext}", bg = "Light Blue", font = (20), fg = "black")
        original.place(x=600, y=120)

        self.mediator.disable_button("Decrypt_button")
        self.mediator.enable_button("Generate_button")
        self.mediator.enable_button("Validate_button")

    def power_value(self, value, key, modulus):
        """
        Calculates the power of a integer as well as modding the value

        This subfunction is used instead of the normal line of code, (value**key) % modulus
        as this would usually produce values incredibly large that the system would not be able
        to compute and would crash the program

        Args:
        value (int): base value being powered
        key (int): Power value being used with value
        modulus (int): The modulus value being used to encrypt with

        Returns:
        power_value (int): The new value produced, which represents part of the palintext encrypted

        This link was used as a basis for the power_value function:
        https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/
        """

        power_value = 1
        for values in range(key):
            if key & 1:
                power_value = (power_value * value)
                power_value = power_value % modulus
            key = key // 2
            value = (value * value)
            value = value % modulus
        return power_value


