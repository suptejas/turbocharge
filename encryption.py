from cryptography.fernet import Fernet
from getpass import getpass

# Getting a password from user
password = getpass('Enter your password: ')

# Class to manage password-related information
class PasswordManager:

    # Encodes a given string
    def encode(self, password):
        bytekey = Fernet.generate_key()
        cipher_suite = Fernet(bytekey)
        byte_password = bytes(password, 'utf-8')
        if password in globals():
            del password
        encrypted_password = cipher_suite.encrypt(byte_password)
        return encrypted_password, cipher_suite 

    # Decodes a given string
    def decode(self ,cipher_suite, encrypted_password):
        if password in globals():
            raise MemoryError('Password Is Not Encrypted And Is Insecure!')
        decoded_string = cipher_suite.decrypt(encrypted_password).decode('utf-8')
        return decoded_string

# Initialising a new instance of PasswordManager()
password_manager = PasswordManager()
# Encryped password and cipher suite need to be passed on to other screens
encrypted_password, cipher_suite = password_manager.encode(password)
print(encrypted_password)
# The below lines should only be called when needed. After used, the decoded password must be deleted using del decoded_password
decoded_password = password_manager.decode(cipher_suite, encrypted_password)
